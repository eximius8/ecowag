from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail_headless_preview.models import HeadlessMixin


class BlogIndexPage(HeadlessMixin, Page):    
    subpage_types = ['blog.BlogPage']
    max_count = 1


class BlogPage(HeadlessMixin, Page):
    parent_page_types = ['blog.BlogIndexPage']

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = StreamField([        
        ('paragraph', blocks.RichTextBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('feed_image'),
        FieldPanel('body'),
    ]

    api_fields = [
        APIField('feed_image'),
        APIField('body'),       
    ]
