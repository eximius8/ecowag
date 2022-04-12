from wagtail.core.blocks import StructBlock, \
    FloatBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource


class Solubility(StructBlock):
    value = FloatBlock(
        label='Растворимость компонента отхода (вещества) в воде при 20° C',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'Растворимость'


class Cnas(StructBlock):
    value = FloatBlock(
        label='Насыщающая концентрация вещества в воздухе при 20° C и нормальном давлении [мг/м3]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'Насыщающая концентрация вещества'


class Kow(StructBlock):
    value = FloatBlock(
        label='Коэффициент распределения в системе октанол/вода при 20° C',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'Коэффициент распределения Kow'


class BOD5(StructBlock):
    value = FloatBlock(
        label='Биологическое потребление кислорода, выраженное в миллилитрах O2/л за 5 суток',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'Биологическое потребление кислорода БПК5'


class COD(StructBlock):
    value = FloatBlock(
        label='Химическое потребление кислорода, выраженное в миллилитрах O2/100 л',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'Химическое потребление кислорода ХПК'
