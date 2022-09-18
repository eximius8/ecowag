from pylatex import Document, Section, MiniPage, Command, Package, MultiColumn, Section
from pylatex.table import Tabu
from substance.models import Substance
import os
from pylatex.utils import bold, NoEscape
from pylatex.basic import LineBreak
from pylatex.math import Math

from .bibliog import Bibliogr


class WasteReport(Document):

    def __init__(self, name, fkko, k, safety_class, components):
        geometry_options = {"left": "20mm", "right": "20mm", "top": "8mm", "bottom": "20mm"}
        super().__init__('basic',geometry_options=geometry_options)      
        self.documentclass = Command('documentclass', options=['12pt',], arguments=['article'])

        self.name = name
        self.fkko = fkko
        self.k = k
        self.safety_class = safety_class
        self.components = components
        self.props = {}
        self.litsources = {}
    
    
    def create_comp_table(self):
        self.append(LineBreak())
        self.append(Command("scriptsize"))
        total_concp = 0
        has_known_components = False # flag that the waste has components
        #has_soil_components = False  
        

        with self.create(Tabu(r"|X[2.2]|X[c]|X[c]|X[c]|X[c]|X[c]|X[c]|X[c]|", to=r"\textwidth", width=8)) as data_table:
            data_table.add_hline()            
            data_table.add_row(["Компонент",
                                "Сод., \%",
                                "$C_i$, мг/кг",
                                "$X_i$",
                                "$Z_i$",
                                "$\lg W_i$",
                                "$W_i$, мг/кг",
                                "$K_i$"],
                                color="gray", escape=False)
            data_table.add_hline()
            for id, conc in self.components.items():
                component = Substance.objects.get(pk=id)
                name = component.title
                if component.x_value_lit_source:
                    name = NoEscape(name + r"\footnotemark[1]")                    
                    has_known_components = True
                
                data_table.add_row([name,
                                    "%.2f" % (conc/1e4),
                                    "%.0f" % conc, 
                                    "%.2f" % component.get_x(), 
                                    "%.2f" % component.get_z(), 
                                    "%.2f" % component.get_log_w(), 
                                    "%.0f" % component.get_w(), 
                                    "%.1f" % component.get_k(conc)])                
                total_concp += conc/1e4      
                data_table.add_hline()                

            
            data_table.add_row(( "Компонентов учтено", "%.0f" % total_concp + " %", MultiColumn(6, align='r|', data='')))
            data_table.add_hline()    
            data_table.add_row([MultiColumn(7, align='|r|', data='Показатель K степени опасности отхода:'), "%.1f" % self.k])
            data_table.add_hline()
            data_table.add_row((MultiColumn(7, align='|r|', data='Класс опасности отхода:'), self.safety_class))
            data_table.add_hline()

        if has_known_components:
           with open(f'{os.path.dirname(os.path.abspath(__file__))}/templates/footnote.tex', 'r') as f:
            self.append(NoEscape(f.read()))
     #   if has_soil_components:
    #        self.append(NoEscape(r"\footnotetext[2]{Концентрация не превышает содержание в основных типах почв, принято W=10\textsuperscript{6} (МПР 536)}"))


        self.append(Command("normalsize"))
        self.append(Command("bigskip"))    
        self.append(LineBreak())

    def fill_document(self):
        """Add a section, a subsection and some text to the document."""
        self.append(Section('Протокол расчета класса опасности отхода'))
        self.create_head("Наименование отхода:", self.name)        
        self.append(Command("bigskip"))
        self.append(LineBreak()) 
        if self.fkko:
            self.create_head("Код ФККО:", self.fkko)
            self.append(Command("bigskip"))
            self.append(LineBreak())
        
        with open(f'{os.path.dirname(os.path.abspath(__file__))}/templates/safety.tex', 'r') as f:
            self.append(NoEscape(f.read()))

        self.create_comp_table()   

        with open(f'{os.path.dirname(os.path.abspath(__file__))}/templates/method.tex', 'r') as f:
            self.append(NoEscape(f.read()))

        for id in self.components.keys():
            component = Substance.objects.get(pk=id)          
            self.print_component_data(component)         


        #self.create_bibliography()

        self.append(Command("bigskip"))
        with open(f'{os.path.dirname(os.path.abspath(__file__))}/templates/shorthands.tex', 'r') as f:
            self.append(NoEscape(f.read()))
    
    def print_component_data(self, component):
        
        self.append(f'Первичные показатели опасности компонента: {component.title}')
        self.append(LineBreak())
        self.append(LineBreak())
        self.append(Command("scriptsize"))
        
        with self.create(Tabu(r"|X[3]|X[c]|X[c]|X[c]|", to=r"\textwidth", width=4)) as data_table:
            data_table.add_hline()            
            data_table.add_row(["Показатель опасности",
                                "Значения показателя",
                                "Балл",
                                "Источник информации"], 
                                mapper=bold,
                                color="lightgray")
            data_table.add_hline()
           
            """ for prop in props:
                sources = ""
                for litsource in prop['literature_source']:
                    self.litsources[litsource['name']] = litsource['latexpart']
                    sources +=  "\\" + f'cite{{{litsource["name"]}}}' 


                data_table.add_row([prop['name'], prop['value'], prop['score'], NoEscape(sources)]) 
                data_table.add_hline() """
            data_table.add_row((
                "Показатель информационного обеспечения",  
                MultiColumn(3, align='l|', 
                data=Math(data=f"Binf={component.b_inf}", 
                inline=True))))
            data_table.add_hline()
        self.append(Command("normalsize"))        
        self.append(LineBreak())

    
    def create_bibliography(self):
        if self.litsources:
            with self.create(Bibliogr(arguments="9")) as environment:            
                for name, latexp in self.litsources.items():   
                    environment.append(Command('bibitem',name))
                    environment.append(NoEscape(latexp))
                    #self.append(LineBreak())   
    
    def create_preamble(self):

        # packages
        self.packages.append(Package(name='fontenc', options="T2A"))
        self.packages.append(Package(name='inputenc', options="utf8"))
        self.packages.append(Package(name='babel', options="russian"))
        self.packages.append(Package(name='fixltx2e'))
        self.packages.append(Package(name='titlesec'))
        self.packages.append(Package(name='lmodern'))
        
        # preamble
        self.preamble.append(NoEscape(r"\titleformat{\section}[block]{\Large\bfseries\filcenter}{}{1em}{}"))
        self.preamble.append(NoEscape(r"\renewcommand{\arraystretch}{1.5}"))
        # bibliography
        
    
    def create_head(self, param, value):        
        with self.create(MiniPage(width=r"0.27\textwidth")):
            self.append(param)            
        with self.create(MiniPage(width=r"0.68\textwidth")):
            self.append(bold(value))   
            



        
        
        