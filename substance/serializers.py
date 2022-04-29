from rest_framework import serializers
from substance.models import Substance

def component_exists(value):

    try:
        Substance.objects.get(pk=value)
    except Substance.DoesNotExist:
        raise serializers.ValidationError(f'Компонент {value} не найден.')

class CommponSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(min_value=0, validators=[component_exists,])
    concentration = serializers.FloatField(
        required=True,
        min_value=0., max_value=100.)


class WasteSerializer(serializers.Serializer):

    components = CommponSerializer(required=True, many=True)
    # name = serializers.CharField(max_length=200)
    # fkko = serializers.CharField(max_length=30)

    def validate_components(self, comps):        
        sum_conc = 0
        for component in comps:
            sum_conc += float(component['concentration'])
        if sum_conc > 100:
            raise serializers.ValidationError("Сумма всех концентраций не может быть больше 100!")
