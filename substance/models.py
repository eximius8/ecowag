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
    ], block_counts={
            'SafetyClassSoil': {'max_num': 1}, 
            'PDKp': {'max_num': 1},
            'ODKp': {'max_num': 1},
    }, null=True, blank=True)

    dwprops = StreamField([
        ('SafetyClassDrinkWater', dwblocks.SafetyClassDrinkWater()),
        ('PDKw', dwblocks.PDKw()),        
        ('ODUw', dwblocks.ODUw()),
        ('OBUVw', dwblocks.OBUVw()),
        
    ], block_counts={
            'SafetyClassDrinkWater': {'max_num': 1}, 
            'PDKw': {'max_num': 1},
            'ODUw': {'max_num': 1},
            'OBUVw': {'max_num': 1},
    }, null=True, blank=True)

    fwprops = StreamField([
        ('SafetyClassFishWater', fwblocks.SafetyClassFishWater()),
        ('PDKfw', fwblocks.PDKfw()),        
        ('OBUVfw', fwblocks.OBUVfw()),
        
    ], block_counts={
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
    ], block_counts={
            'SafetyClassAir': {'max_num': 1}, 
            'PDKss': {'max_num': 1},
            'PDKmr': {'max_num': 1},
            'PDKrz': {'max_num': 1},
            'OBUVair': {'max_num': 1},
    }, null=True, blank=True)

    ecoprops = StreamField([
        ('Persistancy', ecoblocks.Persistancy()),
        ('Bioaccum', ecoblocks.Bioaccum()),
        
    ], block_counts={
            'Persistancy': {'max_num': 1},
            'Bioaccum': {'max_num': 1},
    }, null=True, blank=True)

    ldprops = StreamField([
        ('LD50', ldblocks.LD50()),
        ('LC50', ldblocks.LC50()),
        ('LC50water', ldblocks.LC50water()),
        
    ], block_counts={
            'LD50': {'max_num': 1},
            'LC50': {'max_num': 1},
            'LC50water': {'max_num': 1},
    }, null=True, blank=True)

    foodprops = StreamField([
        ('PDKpp', foodblocks.PDKpp()),
        ('MDS', foodblocks.MDS()),
        ('MDU', foodblocks.MDU()),
        
    ], block_counts={
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
    ]

    def get_prop_count(self):
        """
        Число свойств, учитываемых в расчете 
        """
        count = 0
        props_as_list = list(self.soilprops) + list(self.dwprops) + list(self.fwprops) + \
            list(self.airprops) + list(self.ldprops) + list(self.foodprops) + \
            list(self.props) + list(self.ecoprops)
        all_blocks = [a.block_type for a in props_as_list]
        single_props = ['SafetyClassSoil', 'LD50', 'LC50', 'LC50water', 'SafetyClassFishWater', 
        'Persistancy', 'Bioaccum', 'SafetyClassDrinkWater', 'SafetyClassAir', 'Kow']
        for prop in single_props:
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


    @property
    def get_x(self):
        """
        относительный параметр опасности компонента отхода для окружающей среды
        """
        if self.x_value:
            return self.x_value
        return "1"
    
    def clean(self, *args, **kwargs):

        if self.x_value and not self.x_value_lit_source:
            raise ValidationError(
                {'x_value_lit_source': ['Если задан X, необходимо задать источник',]})
        elif self.x_value_lit_source and not self.x_value:
            raise ValidationError(
                {'x_value': ['Если задан источник, необходимо задать X',]})
        return super().clean(*args, **kwargs)
        