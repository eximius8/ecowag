from wagtail.blocks import FloatBlock, ChoiceBlock
from streams.structvalues import SourceStructBlock, ClassStructValue, PDKfwStructValue


class SafetyClassFishWater(SourceStructBlock):
    value = ChoiceBlock(
        label='Класс опасности в воде рыбохозяйственного значения',
        choices=[
                ('1', 'I класс'),
                ('2', 'II класс'),
                ('3', 'III класс'),
                ('4', 'IV класс'),
            ],
        required=True,)
    abbr = 'Класс опасности в воде водных объектов рыбохозяйственного значения'
    long_name = 'Класс опасности в воде водных объектов рыбохозяйственного значения'

    class Meta:
        icon = 'image'
        label = 'Класс опасности в воде рыбохозяйственного значения'
        value_class = ClassStructValue


class PDKfw(SourceStructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в воде рыбохозяйственного значения (ПДКрх) [мг/л]',
        required=True, min_value=0)
    abbr = 'ПДКр.х. (мг/л)'
    long_name = 'Предельно допустимая концентрация вещества в воде водных '+ \
        'объектов рыбохозяйственного значения'

    class Meta:
        icon = 'cup'
        label = 'ПДК в воде рыбохозяйственного значения'
        value_class = PDKfwStructValue


class OBUVfw(SourceStructBlock):
    value = FloatBlock(
        label='Ориентировочно безопасные уровни воздействия в воде рыбохозяйственного значения (ОБУВ) [мг/л]',
        required=True, min_value=0)
    abbr = 'ОБУВр.х. (мг/л)'
    long_name = 'Ориентировочный безопасный уровень воздействия ' +\
        'концентрация вещества в воде водных объектов рыбохозяйственного значения'

    class Meta:
        icon = 'cup'
        label = 'ОБУВ в воде рыбохозяйственного значения'
        value_class = PDKfwStructValue
