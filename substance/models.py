#from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
import streams.blocks as blocks
from wagtail.admin.edit_handlers import StreamFieldPanel

class Substance(Page):


    props = StreamField([
        ('PDKp', blocks.PDKp())
    ])


    content_panels = Page.content_panels + [
        StreamFieldPanel('props'),
    ]
