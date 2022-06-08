from wagtail.blocks import ChoiceBlock, FloatBlock
from streams.structvalues import SourceStructBlock, ClassStructValue, PDKsoilStructValue


class SafetyClassSoil(SourceStructBlock):
    value = ChoiceBlock(
        label='Класс опасности в почве',
        choices=[
                ('1', 'I класс'),
                ('2', 'II класс'),
                ('3', 'III класс'),
                ('4', 'не установлен'),
            ],
        required=True,)
    abbr = 'Класс опасности в почве'
    long_name = 'Класс опасности в почве' 

    class Meta:
        icon = 'image'
        label = 'Класс опасности в почве'
        value_class = ClassStructValue


class PDKp(SourceStructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в почве (ПДКп) [мг/кг]',
        required=True, min_value=0)
    abbr = 'ПДК в почве (мг/кг)'
    long_name = 'Предельно допустимая концентрация вещества в почве'

    class Meta:
        icon = 'image'
        label = 'ПДК в почве'
        value_class = PDKsoilStructValue


class ODKp(SourceStructBlock):
    value = FloatBlock(
        label='Ориентировочно допустимые концентрации в почве (ОДК) [мг/кг]',
        required=True, min_value=0)
    abbr = 'ОДК в почве (мг/кг)'
    long_name = 'Ориентировочно допустимая концентрация вещества в почве'

    class Meta:
        icon = 'image'
        label = 'ОДК в почве'
        value_class = PDKsoilStructValue
