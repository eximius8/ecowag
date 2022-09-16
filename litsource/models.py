from django.db import models
from django.core.exceptions import ValidationError
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.admin.panels import FieldPanel
from pybtex.database import parse_string
from uuid import uuid4


def validate_bibtex(value):    
    try:
        articles = parse_string(value, "bibtex")
    except:
        raise ValidationError(
            "Поле имеет неверный формат bibtex",
            params={'value': value},
        )
    if len(articles.entries) != 1:
        raise ValidationError(
            "Поле имеет неверный формат bibtex",
            params={'value': value},
        )

@register_snippet
class LitSource(index.Indexed, models.Model):

    name = models.CharField(
        verbose_name='Название источника',
        help_text='Название источника будет показано на вебстранице рядом со свойством' +
        ' - можно указать короткое название (например Приказ Минприроды N 536)',
        blank=False, null=False, max_length=200, unique=True)
    bibtexdata = models.TextField(
        verbose_name='Строка bibtex',
        help_text='Укажите ссылку на документ в формате bibtex. '+
        'После сохранения тэг статьи будет изменен на уникальный. Например: ' + 
        """@article{dmitrievgost,
                    title={ГОСТ ГОСТу-рознь},
                    author={Дмитриев, Евгений Аристархович},
                    journal={Гражданская защита}
                    }""",
    blank=False, null=False, max_length=2000, validators=[validate_bibtex])
    
    source_url = models.URLField(
        blank=True, 
        null=True,
        max_length=500, 
        verbose_name="Url cсылка на источник (при наличии)")
    pannels = [        
        FieldPanel('name'),
        FieldPanel('source_url'),
        FieldPanel('bibtexdata'),
    ]

    search_fields = [
        index.SearchField('name', partial_match=True),
    ]

    def __str__(self) -> str:
        return self.name
    
    def get_bibitem_text(self):
        latexdata = {}
        latexdata['name'] = 'source' + str(self.pk)
        latexdata['main'] = self.fullname
    
    def save(self, *args, **kwargs):

        articles = parse_string(self.bibtexdata, "bibtex")
        article_key = next(iter(articles.entries))
        article = articles.entries[article_key]
        article.key = 'id' + uuid4().hex
        self.bibtexdata = article.to_string('bibtex')
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Источник литературы'
        verbose_name_plural = 'Источники литературы'
