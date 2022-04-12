from wagtail.core.blocks import StructBlock, \
    FloatBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource


class LD50(StructBlock):
    value = FloatBlock(
        label='Средняя смертельная доза компонента в миллиграммах действующего вещества на 1 кг'+
        ' живого веса, вызывающая гибель 50% подопытных'+
        ' животных при однократном пероральном введении в унифицированных условиях [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'LD50 полулетальная доза'


class LC50(StructBlock):
    value = FloatBlock(
        label='Средняя смертельная концентрация вещества, вызывающая гибель'+
        ' 50% подопытных животных при ингаляционном поступлении в унифицированных условиях [мг/м3]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'LС50 полулетальная доза'


class LC50water(StructBlock):
    value = FloatBlock(
        label='Средняя смертельная концентрация вещества в воде,'+
        ' вызывающая гибель 50% всех взятых в опыт гидробионтов (например, рыб) через 96 часов [мг/л/96 ч]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'LC50водн полулетальная доза'
