from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.admin.panels import FieldPanel


@register_snippet
class LitSource(index.Indexed, models.Model):

    name = models.CharField(
        verbose_name='Название источника',
        help_text='Название источника будет показано на вебстранице рядом со свойством' +
        ' - можно указать короткое название (например Приказ Минприроды N 536)',
        blank=False, null=False, max_length=200, unique=True)
    # year = models.IntegerField()
    # тип источника book, article и т.п.
    fullname = models.CharField(
        verbose_name='Полное название источника',
        help_text='Полное название источника будет использовано при формировании pdf отчета - ' +
        '(например Приказ Министерства природных ресурсов и экологии РФ от 4 декабря 2014 г. N 536 '+
        '"Об утверждении Критериев отнесения отходов к I-V классам опасности по степени негативного воздействия на окружающую среду")',
        blank=False, null=False, max_length=500)
    
    CHOICES = (
        ('gost', 'Стандарт'),        
        ('article', 'Статья'),
        ('book', 'Книга (Монография)'),        
    )
    source_type = models.CharField(
        blank=False,
        choices=CHOICES,  
        max_length=10, 
        default="article")
    source_url = models.URLField(
        blank=True, 
        null=True,
        max_length=500, 
        verbose_name="Url cсылка на источник (при наличии)")
    pannels = [
        FieldPanel('source_type'),
        FieldPanel('name'),
        FieldPanel('fullname'),
        FieldPanel('source_url'),
    ]

    search_fields = [
        index.SearchField('name', partial_match=True),
        index.SearchField('fullname', partial_match=True),
    ]

    def __str__(self) -> str:
        return self.name
    
    def get_bibitem_text(self):
        latexdata = {}
        latexdata['name'] = 'source' + str(self.pk)
        latexdata['main'] = self.fullname

    class Meta:
        verbose_name = 'Источник литературы'
        verbose_name_plural = 'Источники литературы'
