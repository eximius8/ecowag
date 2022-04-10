from curses import panel
from tabnanny import verbose
from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel


@register_snippet
class LitSource(index.Indexed, models.Model):

    name = models.CharField(
        verbose_name='Название источника',
        help_text='Укажите название источника (например Приказ Минприроды N 536)',
        blank=False, null=False, max_length=200, unique=True)

    pannels = [
        FieldPanel('name'),
    ]

    search_fields = [
        index.SearchField('name', partial_match=True),
    ]

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Источник литературы'
        verbose_name_plural = 'Источники литературы'
