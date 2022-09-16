from wagtail.blocks import FloatBlock
from streams.structvalues import SourceStructBlock
from wagtail.blocks import StructValue
import math


class Solubility(SourceStructBlock):
    value = FloatBlock(
        label='Растворимость компонента отхода (вещества) в воде при 20° C (мг/л)',
        required=True, min_value=0)
    abbr = 'Растворимость (мг/л)'
    long_name = 'Растворимость компонента отхода (вещества) в воде при 20° C' 

    class Meta:
        icon = 'cup'
        label = 'Растворимость'


class Cnas(SourceStructBlock):
    value = FloatBlock(
        label='Насыщающая концентрация вещества в воздухе при 20° C и нормальном давлении [мг/м3]',
        required=True, min_value=0)
    abbr = 'Снас (мг/м3)'
    long_name = 'Насыщающая концентрация вещества в воздухе при 20° C и нормальном давлении' 

    class Meta:
        icon = 'cup'
        label = 'Насыщающая концентрация вещества'


class KowStructValue(StructValue):
    
    @property
    def Bj(self):
        value = self.get('value')
        logkw = math.log10(value)
        if logkw > 4:
            return 1
        elif logkw >= 2:
            return 2
        elif logkw >= 0:
            return 3
        return 4


class Kow(SourceStructBlock):
    value = FloatBlock(
        label='Коэффициент распределения в системе октанол/вода при 20° C',
        required=True, min_value=0)
    abbr = 'Коэффициент распределения Kow'
    long_name = 'Коэффициент распределения в системе октанол/вода при 20° C' 

    class Meta:
        icon = 'cup'
        label = 'Коэффициент распределения Kow'
        value_class = KowStructValue


class BOD5(SourceStructBlock):
    value = FloatBlock(
        label='Биологическое потребление кислорода, выраженное в миллилитрах O2/л за 5 суток',
        required=True, min_value=0)
    abbr = 'БПК5'
    long_name = 'Биологическое потребление кислорода, выраженное в миллилитрах O2/л за 5 суток' 

    class Meta:
        icon = 'cup'
        label = 'Биологическое потребление кислорода БПК5'


class COD(SourceStructBlock):
    value = FloatBlock(
        label='Химическое потребление кислорода, выраженное в миллилитрах O2/100 л',
        required=True, min_value=0)
    abbr = 'Химическое потребление кислорода ХПК'
    long_name = 'Химическое потребление кислорода, выраженное в миллилитрах O2/100 л' 

    class Meta:
        icon = 'cup'
        label = 'Химическое потребление кислорода ХПК'
