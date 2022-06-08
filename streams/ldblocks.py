from wagtail.blocks import FloatBlock
from streams.structvalues import SourceStructBlock, LC50StructValue, LD50StructValue, LC50wStructValue


class LD50(SourceStructBlock):
    value = FloatBlock(
        label='Средняя смертельная доза компонента в миллиграммах действующего вещества на 1 кг'+
        ' живого веса, вызывающая гибель 50% подопытных'+
        ' животных при однократном пероральном введении в унифицированных условиях [мг/кг]',
        required=True, min_value=0)
    abbr = 'LD50 (мг/кг)'
    long_name = 'Средняя смертельная доза компонента в миллиграммах действующего вещества на 1 кг' + \
        ' живого веса, вызывающая гибель 50% подопытных'+ \
        ' животных при однократном пероральном введении в унифицированных условиях [мг/кг]' 

    class Meta:
        icon = 'cup'
        label = 'LD50 полулетальная доза'
        value_class = LD50StructValue


class LC50(SourceStructBlock):
    value = FloatBlock(
        label='Средняя смертельная концентрация вещества, вызывающая гибель'+
        ' 50% подопытных животных при ингаляционном поступлении в унифицированных условиях [мг/м3]',
        required=True, min_value=0)
    abbr = 'LC50 (мг/м3)'
    long_name = 'Средняя смертельная концентрация вещества, вызывающая гибель' + \
        ' 50% подопытных животных при ингаляционном поступлении в унифицированных условиях [мг/м3]'

    class Meta:
        icon = 'cup'
        label = 'LС50 полулетальная доза'
        value_class = LC50StructValue


class LC50water(SourceStructBlock):
    value = FloatBlock(
        label='Средняя смертельная концентрация вещества в воде,'+
        ' вызывающая гибель 50% всех взятых в опыт гидробионтов (например, рыб) через 96 часов [мг/л/96 ч]',
        required=True, min_value=0)
    abbr = 'LCводн50 (мг/л/96 ч)'
    long_name = 'Средняя смертельная концентрация вещества в воде,' + \
        ' вызывающая гибель 50% всех взятых в опыт гидробионтов (например, рыб) через 96 часов [мг/л/96 ч]'

    class Meta:
        icon = 'cup'
        label = 'LC50водн полулетальная доза'
        value_class = LC50wStructValue
