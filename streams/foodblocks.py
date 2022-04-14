from wagtail.core.blocks import StructBlock, \
    FloatBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource
from .structvalues import APIRepresentationMixin, PDKppStructValue


class PDKpp(APIRepresentationMixin, StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация вещества в пищевых продуктах [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)
    abbr = 'ПДКпп (мг/кг)'
    long_name = 'Предельно допустимая концентрация вещества в пищевых продуктах'

    class Meta:
        icon = 'cup'
        label = 'ПДК в пищевых продуктах'
        value_class = PDKppStructValue


class MDS(APIRepresentationMixin, StructBlock):
    value = FloatBlock(
        label='Максимально допустимое содержание [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)
    abbr = 'МДС (мг/кг)'
    long_name = 'Максимально допустимое содержание вещества в пищевых продуктах'

    class Meta:
        icon = 'cup'
        label = 'МДС в пищевых продуктах'
        value_class = PDKppStructValue


class MDU(APIRepresentationMixin, StructBlock):
    value = FloatBlock(
        label='Максимально допустимый уровень [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)
    abbr = 'МДУ (мг/кг)'
    long_name = 'Максимально допустимый уровень вещества в пищевых продуктах'

    class Meta:
        icon = 'cup'
        label = 'МДУ в пищевых продуктах'
        value_class = PDKppStructValue
