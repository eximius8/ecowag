from wagtail.core.blocks import StructBlock, \
    FloatBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource


class PDKpp(StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация вещества в пищевых продуктах [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'ПДК в пищевых продуктах'


class MDS(StructBlock):
    value = FloatBlock(
        label='Максимально допустимое содержание [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'МДС в пищевых продуктах'


class MDU(StructBlock):
    value = FloatBlock(
        label='Максимально допустимый уровень [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'МДУ в пищевых продуктах'
