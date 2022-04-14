from wagtail.core.blocks import StructValue
from litsource.serializers import LitSourceSerializer


class ClassStructValue(StructValue):

    @property
    def Bj(self):
        value = self.get('value')
        return float(value)


class APIRepresentationMixin:

    def get_api_representation(self, value, context=None):

        api_json = {}
        if value:
            if 'Bj' in dir(value):
                api_json['B'] = value.Bj
            api_json['value'] = value['value']
            api_json['abbr'] = self.abbr
            api_json['name'] = self.long_name
            api_json['source'] = LitSourceSerializer(value['source']).data
            return api_json

def get_b(value, low, medium, high):

    if value < low:
        return 1.
    if value <= medium:
        return 2.
    if value <= high:
        return 3.
    return 4.


class PDKsoilStructValue(StructValue):
    
    @property
    def Bj(self):
        value = self.get('value')
        return get_b(value, 1, 10, 100)


class PDKairStructValue(StructValue):
    
    @property
    def Bj(self):
        value = self.get('value')
        return get_b(value, 0.01, 0.1, 1)