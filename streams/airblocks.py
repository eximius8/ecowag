from wagtail.core.blocks import FloatBlock, ChoiceBlock
from .structvalues import ClassStructValue, PDKairStructValue, SourceStructBlock


class PDKss(SourceStructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в воздухе средне-суточное зоны (ПДКсс) [мг/м3]',
        required=True, min_value=0)
    abbr = 'ПДКс.с. (мг/м3)'
    long_name = 'Предельно допустимая концентрация вещества среднесуточная в атмосферном воздухе населенных мест' 

    class Meta:
        icon = 'image'
        label = 'ПДК в воздухе средне-суточное'
        value_class = PDKairStructValue


class PDKmr(SourceStructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в воздухе максимальная разовая (ПДКмр) [мг/м3]',
        required=True, min_value=0)
    abbr = 'ПДКм.р. (мг/м3)'
    long_name = 'Предельно допустимая концентрация вещества максимально разовая в атмосферном воздухе населенных мест'

    class Meta:
        icon = 'image'
        label = 'ПДК в воздухе максимальная разовая'
        value_class = PDKairStructValue


class PDKrz(SourceStructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в воздухе рабочей зоны (ПДКрз) [мг/м3]',
        required=True, min_value=0)
    abbr = 'ПДКр.з. (мг/м3)'
    long_name = 'Предельно допустимая концентрация вещества в атмосферном воздухе рабочей зоны'

    class Meta:
        icon = 'image'
        label = 'ПДК в воздухе рабочей зоны'


class OBUVair(SourceStructBlock):
    value = FloatBlock(
        label='Ориентировочно безопасные уровни воздействия в воздухе [мг/м3]',
        required=True, min_value=0)
    abbr = 'ОБУВ (мг/м3)'
    long_name = 'Ориентировочный безопасный уровень воздействия в атмосферном воздухе населенных мест'

    class Meta:
        icon = 'image'
        label = 'ОБУВ в воздухе'
        value_class = PDKairStructValue

class SafetyClassAir(SourceStructBlock):
    value = ChoiceBlock(
        label='Класс опасности в воздухе',
        choices=[
                ('1', 'I класс'),
                ('2', 'II класс'),
                ('3', 'III класс'),
                ('4', 'IV класс'),
            ],
        required=True,)
    abbr = 'Класс опасности в атмосферном воздухе'
    long_name = 'Класс опасности в атмосферном воздухе' 

    class Meta:
        icon = 'image'
        label = 'Класс опасности в воздухе'
        value_class = ClassStructValue
