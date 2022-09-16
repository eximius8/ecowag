from wagtail.blocks import FloatBlock
from .structvalues import SourceStructBlock, PDKppStructValue


class PDKpp(SourceStructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация вещества в пищевых продуктах [мг/кг]',
        required=True, min_value=0)
    abbr = 'ПДКпп (мг/кг)'
    long_name = 'Предельно допустимая концентрация вещества в пищевых продуктах'

    class Meta:
        icon = 'cup'
        label = 'ПДК в пищевых продуктах'
        value_class = PDKppStructValue


class MDS(SourceStructBlock):
    value = FloatBlock(
        label='Максимально допустимое содержание [мг/кг]',
        required=True, min_value=0)
    abbr = 'МДС (мг/кг)'
    long_name = 'Максимально допустимое содержание вещества в пищевых продуктах'

    class Meta:
        icon = 'cup'
        label = 'МДС в пищевых продуктах'
        value_class = PDKppStructValue


class MDU(SourceStructBlock):
    value = FloatBlock(
        label='Максимально допустимый уровень [мг/кг]',
        required=True, min_value=0)
    abbr = 'МДУ (мг/кг)'
    long_name = 'Максимально допустимый уровень вещества в пищевых продуктах'

    class Meta:
        icon = 'cup'
        label = 'МДУ в пищевых продуктах'
        value_class = PDKppStructValue
