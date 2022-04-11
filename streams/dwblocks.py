from wagtail.core.blocks import StructBlock, \
    ChoiceBlock, FloatBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource


class SafetyClassDrinkWater(StructBlock):
    value = ChoiceBlock(
        label='Класс опасности в питьевой воде',
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
        label = 'Класс опасности в питьевой воде'


class PDKw(StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в питьевой воде (ПДКв) [мг/л]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'ПДК в питьевой воде'


class ODUw(StructBlock):
    value = FloatBlock(
        label='Ориентировочные допустимые уровни в питьевой воде (ОДУ) [мг/л]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'ОДУ в питьевой воде'


class OBUVw(StructBlock):
    value = FloatBlock(
        label='Ориентировочно безопасные уровни воздействия в питьевой воде (ОБУВ) [мг/л]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'ОБУВ в питьевой воде'
