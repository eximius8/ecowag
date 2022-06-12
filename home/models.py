from wagtail.models import Page


class HomePage(Page):
    subpage_types = ['substance.Substance', 'blog.BlogIndexPage']
    max_count = 1
    #parent_page_types = []
