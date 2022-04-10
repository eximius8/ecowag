#from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
import streams.blocks as blocks
from wagtail.admin.edit_handlers import StreamFieldPanel

class Substance(Page):


    props = StreamField([
        ('PDKp', blocks.PDKp()),
        ('ODKp', blocks.ODKp()),
        ('PDKw', blocks.PDKw()),
        ('SclsSoil', blocks.SafetyClassSoil())
    ], block_counts={
            'PDKp': {'max_num': 1}, 
            'PDKw': {'max_num': 1},
            'ODKp': {'max_num': 1},
            'SclsSoil': {'max_num': 1},       
            },
    )


    content_panels = Page.content_panels + [
        StreamFieldPanel('props'),
    ]
