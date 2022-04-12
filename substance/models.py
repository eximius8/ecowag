#from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import soilblocks, dwblocks, fwblocks, ecoblocks, airblocks, ldblocks

from wagtail.admin.edit_handlers import StreamFieldPanel

class Substance(Page):

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

    content_panels = Page.content_panels + [
        StreamFieldPanel('soilprops', heading='Свойства для почвы'),
        StreamFieldPanel('dwprops', heading='Свойства для питьевой воды'),
        StreamFieldPanel('fwprops', heading='Свойства для воды рыбохозяйственного значения'),
        StreamFieldPanel('airprops', heading='Свойства для воздуха'),
        StreamFieldPanel('ldprops', heading='Летальные свойства'),
        StreamFieldPanel('ecoprops', heading='Поведение в окружающей среде'),
    ]
