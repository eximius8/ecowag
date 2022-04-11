from wagtail.core.blocks import StructBlock, \
    FloatBlock, ChoiceBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource


class SafetyClassFishWater(StructBlock):
    value = ChoiceBlock(
        label='Класс опасности в воде рыбохозяйственного значения',
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
        label = 'Класс опасности в воде рыбохозяйственного значения'


class PDKfw(StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в воде рыбохозяйственного значения (ПДКрх) [мг/л]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'ПДК в воде рыбохозяйственного значения'


class OBUVfw(StructBlock):
    value = FloatBlock(
        label='Ориентировочно безопасные уровни воздействия в воде рыбохозяйственного значения (ОБУВ) [мг/л]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)

    class Meta:
        icon = 'cup'
        label = 'ОБУВ в воде рыбохозяйственного значения'
