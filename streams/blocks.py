from wagtail.core.blocks import StructBlock, \
    FloatBlock, ChoiceBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource

class PDKp(StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в почве (ПДКп) [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'image'
        label = 'ПДК в почве'

class ODKp(StructBlock):
    value = FloatBlock(
        label='Ориентировочно допустимые концентрации в почве (ОДК) [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'image'
        label = 'ОДК в почве'

class SafetyClassSoil(StructBlock):
    value = ChoiceBlock(
        label='Класс опасности в почве',
        choices=[
                ('1', 'I класс'),
                ('2', 'II класс'),
                ('3', 'III класс'),
                ('4', 'не установлен'),
            ],
        required=True,)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'image'
        label = 'Класс опасности в почве'

class PDKw(StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в воде (ПДКв) [мг/л]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'ПДК в воде'