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
    # year = models.IntegerField()
    # тип источника book, article и т.п.
    CHOICES = ( 
        ('prikaz', 'Приказ'),
        ('gost', 'ГОСТ'),
        ('art', 'Статья'),
        ('gn', 'Гигиенические нормативы'),
        ('art', 'Статья'),
        ('sanpin', 'Санитарные (санитарно-эпидемиологические) правила и нормы')
    )
    source_type = models.CharField(blank=False,
                                   choices=CHOICES,  
                                   max_length=10, 
                                   default="art")
    source_url = models.URLField(blank=True, null=True,
                                 max_length=500, verbose_name="Url cсылка на источник (при наличии)")

    pannels = [
        FieldPanel('name'),
        FieldPanel('source_type'),
        FieldPanel('source_url'),
    ]

    search_fields = [
        index.SearchField('name', partial_match=True),
    ]

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Источник литературы'
        verbose_name_plural = 'Источники литературы'
