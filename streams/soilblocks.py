from wagtail.core.blocks import StructBlock, \
    ChoiceBlock, FloatBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource
from .structvalues import ClassStructValue, PDKsoilStructValue, APIRepresentationMixin



class SafetyClassSoil(APIRepresentationMixin, StructBlock):
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
    abbr = 'Класс опасности в почве'
    long_name = 'Класс опасности в почве' 

    class Meta:
        icon = 'image'
        label = 'Класс опасности в почве'
        value_class = ClassStructValue


class PDKp(APIRepresentationMixin, StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в почве (ПДКп) [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)
    abbr = 'ПДК в почве (мг/кг)'
    long_name = 'Предельно допустимая концентрация вещества в почве'    


    class Meta:
        icon = 'image'
        label = 'ПДК в почве'
        value_class = PDKsoilStructValue

class ODKp(APIRepresentationMixin, StructBlock):
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
        value_class = PDKsoilStructValue
