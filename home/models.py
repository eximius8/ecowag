from wagtail.models import Page


class HomePage(Page):
    subpage_types = ['substance.SubstanceIndex', 'blog.BlogIndexPage']
    max_count = 1
    #parent_page_types = []

    class Meta:
        verbose_name = 'Домашняя страница'
