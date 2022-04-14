from wagtail.core.blocks import StructBlock, \
    ChoiceBlock, FloatBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource
from .structvalues import ClassStructValue, APIRepresentationMixin, PDKdwStructValue


class SafetyClassDrinkWater(APIRepresentationMixin, StructBlock):
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
    abbr = 'Класс опасности в питьевой воде'
    long_name = 'Класс опасности в воде водных объектов, используемых для' + \
        'целей питьевого и хозяйственнобытового водоснабжения'

    class Meta:
        icon = 'image'
        label = 'Класс опасности в питьевой воде'
        value_class = ClassStructValue


class PDKw(APIRepresentationMixin, StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в питьевой воде (ПДКв) [мг/л]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)
    abbr = 'ПДКВ (мг/л)'
    long_name = 'Предельно допустимая концентрация вещества ' + \
        'в воде водных объектов, используемых для целей питьевого '+ \
        'и хозяйственнобытового водоснабжения'

    class Meta:
        icon = 'cup'
        label = 'ПДК в питьевой воде'
        value_class = PDKdwStructValue


class ODUw(APIRepresentationMixin, StructBlock):
    value = FloatBlock(
        label='Ориентировочные допустимые уровни в питьевой воде (ОДУ) [мг/л]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)
    abbr = 'ОДУ (мг/л)'
    long_name = 'Ориентировочно допустимый уровень концентрации вещества ' + \
        'в воде водных объектов, используемых для целей питьевого '+ \
        'и хозяйственнобытового водоснабжения'

    class Meta:
        icon = 'cup'
        label = 'ОДУ в питьевой воде'
        value_class = PDKdwStructValue


class OBUVw(APIRepresentationMixin, StructBlock):
    value = FloatBlock(
        label='Ориентировочно безопасные уровни воздействия в питьевой воде (ОБУВ) [мг/л]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)
    abbr = 'ОБУВ (мг/л)'
    long_name = 'Ориентировочный безопасный уровень воздействия концентрации вещества ' + \
        'в воде водных объектов, используемых для целей питьевого '+ \
        'и хозяйственнобытового водоснабжения'

    class Meta:
        icon = 'cup'
        label = 'ОБУВ в питьевой воде'
        value_class = PDKdwStructValue
