from wagtail.core.blocks import StructBlock, \
    ChoiceBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource
from .structvalues import ClassStructValue, APIRepresentationMixin


class Persistancy(APIRepresentationMixin, StructBlock):
    value = ChoiceBlock(
        label='Персистентность',
        choices=[
                ('1', 'Образование более токсичных продуктов, в т.ч. обладающих отдаленными эффектами или новыми свойствами'),
                ('2', 'Образование продуктов с более выраженным влиянием других критериев опасности'),
                ('3', 'Образование продуктов, токсичность которых близка к токсичности исходного вещества'),
                ('4', 'Образование менее токсичных продуктов'),
            ],
        required=True,)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)
    abbr = 'Персистентность'
    long_name = 'Персистентность (трансформация в окружающей среде)'

    class Meta:
        icon = 'image'
        label = 'Персистентность (трансформация в окружающей среде)'
        value_class = ClassStructValue


class Bioaccum(APIRepresentationMixin, StructBlock):
    value = ChoiceBlock(
        label='Биоаккумуляция',
        choices=[
                ('1', 'Выраженное накопление во всех звеньях'),
                ('2', 'Накопление в нескольких звеньях'),
                ('3', 'Накопление в одном из звеньев'),
                ('4', 'Накопление отсутствует'),
            ],
        required=True,)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)
    abbr = 'Биоаккумуляция'
    long_name = 'Биоаккумуляция (поведение в пищевой цепочке)'


    class Meta:
        icon = 'image'
        label = 'Биоаккумуляция (поведение в пищевой цепочке)'
        value_class = ClassStructValue
