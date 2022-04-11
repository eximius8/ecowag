from wagtail.core.blocks import StructBlock, \
    FloatBlock, ChoiceBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource

class PDKss(StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в воздухе средне-суточное зоны (ПДКсс) [мг/м3]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'image'
        label = 'ПДК в воздухе средне-суточное'


class PDKmr(StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в воздухе максимальная разовая (ПДКмр) [мг/м3]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'image'
        label = 'ПДК в воздухе максимальная разовая'


class PDKrz(StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в воздухе рабочей зоны (ПДКрз) [мг/м3]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'image'
        label = 'ПДК в воздухе рабочей зоны'


class OBUVair(StructBlock):
    value = FloatBlock(
        label='Ориентировочно безопасные уровни воздействия в воздухе [мг/м3]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'image'
        label = 'ОБУВ в воздухе'

class SafetyClassAir(StructBlock):
    value = ChoiceBlock(
        label='Класс опасности в воздухе',
        choices=[
                ('1', 'I класс'),
                ('2', 'II класс'),
                ('3', 'III класс'),
                ('4', 'IV класс'),
            ],
        required=True,)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'image'
        label = 'Класс опасности в воздухе'
