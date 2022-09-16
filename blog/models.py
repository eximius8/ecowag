from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail_headless_preview.models import HeadlessMixin
from wagtail.images.api.fields import ImageRenditionField


class BlogIndexPage(HeadlessMixin, Page):    
    subpage_types = ['blog.BlogPage']
    parent_page_types = ['home.HomePage']
    max_count = 1


class BlogPage(HeadlessMixin, Page):
    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []

    img = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=False,
    )

    body = StreamField([        
            ('paragraph', blocks.RichTextBlock()),
        ], 
        use_json_field=True, 
        null=True,
        blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('img'),
        FieldPanel('body'),
    ]

    api_fields = [
        APIField('img'),
        APIField('img_small', serializer=ImageRenditionField('fill-200x100', source='img')),
        APIField('body'),       
    ]
