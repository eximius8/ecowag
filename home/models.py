from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    subpage_types = ['substance.Substance']
