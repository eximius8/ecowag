from wagtail.core.blocks import StructBlock, \
    FloatBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource

class PDKp(StructBlock):
    value = FloatBlock(required=True, min_value=0)
    source = SnippetChooserBlock(LitSource, required=True)

    class Meta:
        icon = 'cup'
