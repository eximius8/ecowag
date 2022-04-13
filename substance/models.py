from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from django.core.exceptions import ValidationError

from streams import soilblocks, dwblocks, fwblocks, \
    ecoblocks, airblocks, ldblocks, propblocks, foodblocks

from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel, \
    FieldPanel, FieldRowPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

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
        ('SclsSoil', soilblocks.SafetyClassSoil()),
        ('PDKp', soilblocks.PDKp()),
        ('ODKp', soilblocks.ODKp()),        
    ], block_counts={
            'PDKp': {'max_num': 1}, 
            'ODKp': {'max_num': 1},
            'SclsSoil': {'max_num': 1},
    }, null=True, blank=True)

    dwprops = StreamField([
        ('SclsDWater', dwblocks.SafetyClassDrinkWater()),
        ('PDKw', dwblocks.PDKw()),        
        ('oduw', dwblocks.ODUw()),
        ('obuvw', dwblocks.OBUVw()),
        
    ], block_counts={
            'SclsDWater': {'max_num': 1}, 
            'PDKw': {'max_num': 1},
            'oduw': {'max_num': 1},
            'obuvw': {'max_num': 1},
    }, null=True, blank=True)

    fwprops = StreamField([
        ('SclsFWater', fwblocks.SafetyClassFishWater()),
        ('PDKfw', fwblocks.PDKfw()),        
        ('obuvfw', fwblocks.OBUVfw()),
        
    ], block_counts={
            'SclsFWater': {'max_num': 1}, 
            'PDKfw': {'max_num': 1},
            'obuvfw': {'max_num': 1},
    }, null=True, blank=True)

    airprops = StreamField([
        ('SclsAir', airblocks.SafetyClassAir()),
        ('PDKss', airblocks.PDKss()),        
        ('PDKmr', airblocks.PDKmr()),
        ('PDKrz', airblocks.PDKrz()),
        ('obuvair', airblocks.OBUVair()),        
    ], block_counts={
            'SclsAir': {'max_num': 1}, 
            'PDKss': {'max_num': 1},
            'PDKmr': {'max_num': 1},
            'PDKrz': {'max_num': 1},
            'obuvair': {'max_num': 1},
    }, null=True, blank=True)

    ecoprops = StreamField([
        ('presistancy', ecoblocks.Persistancy()),
        ('bioaccum', ecoblocks.Bioaccum()),
        
    ], block_counts={
            'presistancy': {'max_num': 1},
            'bioaccum': {'max_num': 1},
    }, null=True, blank=True)

    ldprops = StreamField([
        ('ld50', ldblocks.LD50()),
        ('lc50', ldblocks.LC50()),
        ('lc50water', ldblocks.LC50water()),
        
    ], block_counts={
            'ld50': {'max_num': 1},
            'lc50': {'max_num': 1},
            'lc50water': {'max_num': 1},
    }, null=True, blank=True)

    foodprops = StreamField([
        ('pdkpp', foodblocks.PDKpp()),
        ('mds', foodblocks.MDS()),
        ('mdu', foodblocks.MDU()),
        
    ], block_counts={
            'pdkpp': {'max_num': 1},
            'mds': {'max_num': 1},
            'mdu': {'max_num': 1},
    }, null=True, blank=True)

    props = StreamField([
        ('Kow', propblocks.Kow()),
        ('Solubility', propblocks.Solubility()),
        ('COD', propblocks.COD()),
        ('BOD5', propblocks.BOD5()),
        ('Cnas', propblocks.Cnas()),        
    ], block_counts={
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

    def get_x(self):
        """
        относительный параметр опасности компонента отхода для окружающей среды
        """
        if self.x_value:
            return self.x_value
    
    def clean(self, *args, **kwargs):

        if self.x_value and not self.x_value_lit_source:
            raise ValidationError(
                {'x_value_lit_source': ['Если задан X, необходимо задать источник',]})
        elif self.x_value_lit_source and not self.x_value:
            raise ValidationError(
                {'x_value': ['Если задан источник, необходимо задать X',]})
        return super().clean(*args, **kwargs)
        