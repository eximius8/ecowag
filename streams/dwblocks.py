from wagtail.blocks import ChoiceBlock, FloatBlock
from .structvalues import SourceStructBlock, ClassStructValue, PDKdwStructValue


class SafetyClassDrinkWater(SourceStructBlock):
    value = ChoiceBlock(
        label='Класс опасности в питьевой воде',
        choices=[
                ('1', 'I класс'),
                ('2', 'II класс'),
                ('3', 'III класс'),
                ('4', 'IV класс'),
            ],
        required=True,)
    abbr = 'Класс опасности в питьевой воде'
    long_name = 'Класс опасности в воде водных объектов, используемых для' + \
        'целей питьевого и хозяйственнобытового водоснабжения'

    class Meta:
        icon = 'image'
        label = 'Класс опасности в питьевой воде'
        value_class = ClassStructValue


class PDKw(SourceStructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в питьевой воде (ПДКв) [мг/л]',
        required=True, min_value=0)
    abbr = 'ПДКВ (мг/л)'
    long_name = 'Предельно допустимая концентрация вещества ' + \
        'в воде водных объектов, используемых для целей питьевого '+ \
        'и хозяйственнобытового водоснабжения'

    class Meta:
        icon = 'cup'
        label = 'ПДК в питьевой воде'
        value_class = PDKdwStructValue


class ODUw(SourceStructBlock):
    value = FloatBlock(
        label='Ориентировочные допустимые уровни в питьевой воде (ОДУ) [мг/л]',
        required=True, min_value=0)
    abbr = 'ОДУ (мг/л)'
    long_name = 'Ориентировочно допустимый уровень концентрации вещества ' + \
        'в воде водных объектов, используемых для целей питьевого '+ \
        'и хозяйственнобытового водоснабжения'

    class Meta:
        icon = 'cup'
        label = 'ОДУ в питьевой воде'
        value_class = PDKdwStructValue


class OBUVw(SourceStructBlock):
    value = FloatBlock(
        label='Ориентировочно безопасные уровни воздействия в питьевой воде (ОБУВ) [мг/л]',
        required=True, min_value=0)
    abbr = 'ОБУВ (мг/л)'
    long_name = 'Ориентировочный безопасный уровень воздействия концентрации вещества ' + \
        'в воде водных объектов, используемых для целей питьевого '+ \
        'и хозяйственнобытового водоснабжения'

    class Meta:
        icon = 'cup'
        label = 'ОБУВ в питьевой воде'
        value_class = PDKdwStructValue
