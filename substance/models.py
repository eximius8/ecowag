import math
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.api import APIField
from django.core.exceptions import ValidationError

from streams import soilblocks, dwblocks, fwblocks, \
    ecoblocks, airblocks, ldblocks, propblocks, foodblocks

from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel, \
    FieldPanel, FieldRowPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from streams.structvalues import get_b, get_rev_b


class Substance(Page):

    x_value = models.FloatField(
        blank=True, 
        null=True, 
        verbose_name="X - относительный параметр опасности компонента отхода " +
        "для окружающей среды (если известен - указание источника обязательно)",
        validators=[MinValueValidator(1.0),MaxValueValidator(4.0)])

    x_value_lit_source = models.ForeignKey('litsource.LitSource',
                                    blank=True, 
                                    null=True, 
                                    on_delete=models.SET_NULL, 
                                    related_name='x_value', 
                                    verbose_name='Источник литературы для относительного параметра опаности (если задано числовое значение X, то обязателен)')
                               
    other_names = models.CharField(
        max_length=1000,
        blank=True, 
        default="", 
        verbose_name="Другие названия (через точку с запятой)")
    cas_number = models.CharField(max_length=30,
                                  verbose_name="Регистрационный номер CAS",
                                  blank=True,
                                  validators=[
                                      RegexValidator(
                                          regex=r"\b[1-9]{1}[0-9]{1,6}-\d{2}-\d\b",
                                          message="CAS код для вещества в формате 1111-11-1"),
                                        ])

    soilprops = StreamField([
        ('SafetyClassSoil', soilblocks.SafetyClassSoil()),
        ('PDKp', soilblocks.PDKp()),
        ('ODKp', soilblocks.ODKp()),        
    ], max_num=3, block_counts={
            'SafetyClassSoil': {'max_num': 1}, 
            'PDKp': {'max_num': 1},
            'ODKp': {'max_num': 1},
    }, null=True, blank=True)

    dwprops = StreamField([
        ('SafetyClassDrinkWater', dwblocks.SafetyClassDrinkWater()),
        ('PDKw', dwblocks.PDKw()),        
        ('ODUw', dwblocks.ODUw()),
        ('OBUVw', dwblocks.OBUVw()),        
    ], max_num=4, block_counts={
            'SafetyClassDrinkWater': {'max_num': 1}, 
            'PDKw': {'max_num': 1},
            'ODUw': {'max_num': 1},
            'OBUVw': {'max_num': 1},
    }, null=True, blank=True)

    fwprops = StreamField([
        ('SafetyClassFishWater', fwblocks.SafetyClassFishWater()),
        ('PDKfw', fwblocks.PDKfw()),        
        ('OBUVfw', fwblocks.OBUVfw()),        
    ], max_num=3, block_counts={
            'SafetyClassFishWater': {'max_num': 1}, 
            'PDKfw': {'max_num': 1},
            'OBUVfw': {'max_num': 1},
    }, null=True, blank=True)

    airprops = StreamField([
        ('SafetyClassAir', airblocks.SafetyClassAir()),
        ('PDKss', airblocks.PDKss()),        
        ('PDKmr', airblocks.PDKmr()),
        ('PDKrz', airblocks.PDKrz()),
        ('OBUVair', airblocks.OBUVair()),        
    ], max_num=5, block_counts={
            'SafetyClassAir': {'max_num': 1}, 
            'PDKss': {'max_num': 1},
            'PDKmr': {'max_num': 1},
            'PDKrz': {'max_num': 1},
            'OBUVair': {'max_num': 1},
    }, null=True, blank=True)

    ecoprops = StreamField([
        ('Persistancy', ecoblocks.Persistancy()),
        ('Bioaccum', ecoblocks.Bioaccum()),        
    ], max_num=2, block_counts={
            'Persistancy': {'max_num': 1},
            'Bioaccum': {'max_num': 1},
    }, null=True, blank=True)

    ldprops = StreamField([
        ('LD50', ldblocks.LD50()),
        ('LC50', ldblocks.LC50()),
        ('LC50water', ldblocks.LC50water()),        
    ], max_num=3, block_counts={
            'LD50': {'max_num': 1},
            'LC50': {'max_num': 1},
            'LC50water': {'max_num': 1},
    }, null=True, blank=True)

    foodprops = StreamField([
        ('PDKpp', foodblocks.PDKpp()),
        ('MDS', foodblocks.MDS()),
        ('MDU', foodblocks.MDU()),        
    ], max_num=3, block_counts={
            'PDKpp': {'max_num': 1},
            'MDS': {'max_num': 1},
            'MDU': {'max_num': 1},
    }, null=True, blank=True)

    props = StreamField([
        ('Kow', propblocks.Kow()),
        ('Solubility', propblocks.Solubility()),
        ('COD', propblocks.COD()),
        ('BOD5', propblocks.BOD5()),
        ('Cnas', propblocks.Cnas()),        
    ], max_num=5, block_counts={
            'Kow': {'max_num': 1},
            'Solubility': {'max_num': 1},
            'COD': {'max_num': 1},
            'BOD5': {'max_num': 1},
            'Cnas': {'max_num': 1},
    }, null=True, blank=True)

    content_panels = Page.content_panels + [  
        FieldPanel('cas_number'),
        FieldPanel('other_names', classname="full"), 
        MultiFieldPanel([
            FieldRowPanel(
                [FieldPanel('x_value'),
                 SnippetChooserPanel('x_value_lit_source')]),
        ], heading="Известные параметр X"),
        StreamFieldPanel('soilprops', heading='Свойства для почвы'),
        StreamFieldPanel('dwprops', heading='Свойства для питьевой воды'),
        StreamFieldPanel('fwprops', heading='Свойства для воды рыбохозяйственного значения'),
        StreamFieldPanel('airprops', heading='Свойства для воздуха'),
        StreamFieldPanel('ldprops', heading='Летальные свойства'),
        StreamFieldPanel('foodprops', heading='Содержание в продуктах'),
        StreamFieldPanel('props', heading='Физические, химические и биологические свойства'),
        StreamFieldPanel('ecoprops', heading='Поведение в окружающей среде'),
    ]

    api_fields = [
        APIField('soilprops'),
        APIField('dwprops'),
        APIField('fwprops'),
        APIField('airprops'),
        APIField('ldprops'),
        APIField('foodprops'),
        APIField('props'),
        APIField('ecoprops'),
        APIField('get_x'),
        APIField('get_prop_count'),
        APIField('b_inf'),        
    ]

    single_props = ['SafetyClassSoil', 'LD50', 'LC50', 'LC50water', 'SafetyClassFishWater', 
        'Persistancy', 'Bioaccum', 'SafetyClassDrinkWater', 'SafetyClassAir', 'Kow']
    
    def get_set_props(self):

        props_as_list = list(self.soilprops) + list(self.dwprops) + list(self.fwprops) + \
            list(self.airprops) + list(self.ldprops) + list(self.foodprops) + \
            list(self.props) + list(self.ecoprops)
        return [a.block_type for a in props_as_list]
    
    def get_streams_as_dict(self):
        '''
        Возвращает все свойства как словарь
        '''
        streamflds = [
            self.soilprops, self.dwprops, self.fwprops, self.airprops,
            self.ldprops, self.foodprops, self.props, self.ecoprops
        ]
        stream_dict = {}
        for streamf in streamflds:
            for prop in streamf:
                stream_dict[prop.block_type] = prop.value["value"]
        return stream_dict


    def get_prop_count(self):
        """
        Число свойств, учитываемых в расчете 
        """
        count = 0        
        all_blocks = self.get_set_props()
        for prop in self.single_props:
            if prop in all_blocks:
                count += 1
        if any(x in all_blocks for x in ['PDKp', 'ODKp']):
            count += 1
        if any(x in all_blocks for x in ['PDKw', 'ODUw', 'OBUVw']):
            count += 1
        if any(x in all_blocks for x in ['PDKfw', 'OBUVfw']):
            count += 1
        if any(x in all_blocks for x in ['PDKss', 'PDKmr', 'OBUVair']):
            count += 1
        if any(x in all_blocks for x in ['PDKpp', 'MDS', 'MDU']):
            count += 1
        if all(x in all_blocks for x in ['BOD5', 'COD']):
            count += 1
        if all(x in all_blocks for x in ['Solubility', 'PDKw']):        
            count += 1
        if all(x in all_blocks for x in ['Cnas', 'PDKrz']):        
            count += 1
        if 'Cnas' in all_blocks and any(x in all_blocks for x in ['PDKss', 'PDKmr']):
            count += 1
        return count
    
    def complexBj(self, selfitems, props_in_order):
        '''
        Функция возвращает В для свойства.
        props_in_order - свойства в порядке убывания важности
        selfitems - streamfield
        '''
        all_blocks = [a.block_type for a in selfitems]
        for prop in props_in_order:
            if prop in list(all_blocks):
                for block in selfitems:
                    if block.block_type == prop:
                        return block.value.Bj
        return 0
    
    @property
    def b_inf(self):
        prop_count = self.get_prop_count()
        if prop_count < 6:
            return 1.
        elif prop_count < 9:
            return 2.
        elif prop_count < 11:
            return 3.
        return 4.
    
    def get_sum_complexBj(self):

        sumbj = 0
        sumbj += self.complexBj(self.soilprops, ['PDKp', 'ODKp'])
        sumbj += self.complexBj(self.dwprops, ['PDKw', 'ODUw', 'OBUVw'])
        sumbj += self.complexBj(self.fwprops, ['PDKfw', 'OBUVfw'])
        sumbj += self.complexBj(self.airprops, ['PDKss', 'PDKmr', 'OBUVair'])
        sumbj += self.complexBj(self.foodprops, ['PDKpp', 'MDS', 'MDU'])
        return sumbj
    
    def get_sum_singleBj(self):

        sumbj = 0
        props_as_list = list(self.soilprops) + list(self.dwprops) + list(self.fwprops) + \
            list(self.airprops) + list(self.ldprops) + list(self.foodprops) + \
            list(self.props) + list(self.ecoprops)
        all_blocks = [a for a in props_as_list]
        for prop in all_blocks:
            if prop.block_type in self.single_props:
                sumbj += prop.value.Bj
        
        return sumbj
    
    def get_sum_multiBj(self):
        
        sumbj = 0        
        prop_dict = self.get_streams_as_dict()
        if all(x in prop_dict for x in ['BOD5', 'COD']):
            bd = prop_dict['BOD5'] / prop_dict['COD'] * 100
            sumbj += get_b(bd, 0.1, 1., 10.)
        if all(x in prop_dict for x in ['Solubility', 'PDKw']):
            lgspdk = math.log10(prop_dict['Solubility'] / prop_dict['PDKw'])
            sumbj += get_rev_b(lgspdk, 5., 2., 1.)
        if all(x in prop_dict for x in ['Cnas', 'PDKrz']):
            lgcpdk = math.log10(prop_dict['Cnas'] / prop_dict['PDKrz'])
            sumbj += get_rev_b(lgcpdk, 5., 2., 1.)
        if 'Cnas' in prop_dict and any(x in prop_dict for x in ['PDKss', 'PDKmr']):
            if 'PDKss' in prop_dict:
                pdk = prop_dict['PDKss']
            else:
                pdk = prop_dict['PDKmr']
            lgcpdkss = math.log10(prop_dict['Cnas'] / pdk)
            sumbj += get_rev_b(lgcpdkss, 7., 3.9, 1.6)

        return sumbj

    
    def get_sumBj(self):
        """
        Общее значение B для всех свойств
        """
        return self.get_sum_complexBj() + self.get_sum_singleBj() + self.get_sum_multiBj()
        

    def get_x(self):
        """
        относительный параметр опасности компонента отхода для окружающей среды
        """
        if self.x_value:
            return self.x_value        
        return (self.get_sumBj() + self.b_inf) / (self.get_prop_count() + 1)
    
    def get_z(self):
        """
        унифицированный относительный параметр опасности компонента отхода для окружающей среды
        """        
        return 4./3.*self.get_x()-1./3.
    
    def get_log_w(self):
        """
        Функция считает логарифм от коэффициента степени опасности компонента
        уточнить логарифм десятичный или какой-то другой
        """
        z = self.get_z()
        if 1. <= z <= 2:
            return 4. - 4. / z
        elif 2. < z <= 4:
            return z
        elif 4. < z <= 5:
            return 2. + 4. / (6 - z)
        return 1
    
    def get_w(self):
        """
        Функция считает коэффициента степени опасности компонента       
        если значение w задано в базе возвращает значение из базы
        """
        return 10.**self.get_log_w()    
  
    def get_k(self, conc):
        """
        Показатель опасности компонента отхода 
        conc - концентрация в мг/кг
        если для компонента задана фоновая концентрация в почве и значение conc меньше нее
        принимает W=1e6
        в противном случае считает W согласно методике по свойства
        """
        #if self.land_concentration:
         #   if conc > self.land_concentration:
          #      return conc / self.get_w()
           # return conc/1e6
        return conc / self.get_w()
    
    def clean(self, *args, **kwargs):

        if self.x_value and not self.x_value_lit_source:
            raise ValidationError(
                {'x_value_lit_source': ['Если задан X, необходимо задать источник',]})
        elif self.x_value_lit_source and not self.x_value:
            raise ValidationError(
                {'x_value': ['Если задан источник, необходимо задать X',]})
        return super().clean(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'
