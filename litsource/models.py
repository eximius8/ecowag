from django.db import models
from wagtail.snippets.models import register_snippet


@register_snippet
class LitSource(models.Model):

    name = models.CharField(blank=False, null=False, max_length=200, unique=True)


