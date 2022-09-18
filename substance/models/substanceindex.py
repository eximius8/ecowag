from wagtail_headless_preview.models import HeadlessMixin
from wagtail.models import Page

class SubstanceIndex(HeadlessMixin, Page):

    subpage_types = ['substance.SubstanceType']
    parent_page_types = ['home.HomePage']
    max_count = 1

    class Meta:
        verbose_name = 'Страница компонентов'


class SubstanceType(HeadlessMixin, Page):

    subpage_types = ['substance.Substance']
    parent_page_types = ['substance.SubstanceIndex']

    class Meta:
        verbose_name = 'Тип компонентов'
        verbose_name_plural = 'Типы компонентов'