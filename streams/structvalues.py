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
            api_json['B'] = value.Bj
            api_json['value'] = value['value']
            api_json['abbr'] = self.abbr
            api_json['name'] = self.long_name
            api_json['source'] = LitSourceSerializer(value['source']).data
            return api_json


class PDKsoilStructValue(StructValue):
    
    @property
    def Bj(self):
        value = self.get('value')
        if value < 1:
            return 1.
        if value <= 10:
            return 2.
        if value <= 100:
            return 3.
        return 4.