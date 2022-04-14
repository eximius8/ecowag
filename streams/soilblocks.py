from wagtail.core.blocks import StructBlock, \
    ChoiceBlock, FloatBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from litsource.models import LitSource
from wagtail.core.blocks import StructValue
from litsource.serializers import LitSourceSerializer


class PDKStructValue(StructValue):
    
    @property
    def Bj(self):
        value = self.get('value')
        if value < 1:
            return 1
        if value <= 10:
            return 2
        if value <= 100:
            return 3 
        return 4

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


class PDKp(StructBlock):
    value = FloatBlock(
        label='Предельно допустимая концентрация в почве (ПДКп) [мг/кг]',
        required=True, min_value=0)
    source = SnippetChooserBlock(
        LitSource,
        label="Источник литературы для значения", 
        required=True)
    
    def get_api_representation(self, value, context=None):
      
        if value:
            return {
                'B': value.Bj,
                'value': value['value'],
                'abbr': 'ПДКп (мг/кг)',
                'name': 'Предельно допустимая концентрация вещества в почве',
                'source': LitSourceSerializer(value['source']).data,
            }

    class Meta:
        icon = 'image'
        label = 'ПДК в почве'
        value_class = PDKStructValue

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
        value_class = PDKStructValue
