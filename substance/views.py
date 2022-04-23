from rest_framework.decorators import api_view
from rest_framework.response import Response

from substance.serializers import WasteSerializer
from substance.models import Substance


class Waste:

    def __init__(self, data):

        self.components = []
        for key, val in data.items():            
            self.components += [(Substance.objects.get(pk=key), float(val)),]
    
    def get_summ_K(self):

        k=0.
        for component in self.components:
            k += component[0].get_k(component[1])        
        return k
    
    def get_safety_class(self):               

        k = self.get_summ_K()
        if k <= 10:
            return "V"
        elif 10 < k <= 100:
            return "IV"
        elif 100 < k <= 1000:
            return "III"
        elif 1000 < k <= 10000:
            return "II"
        else:
            return "I"
    
    def get_components(self):

        comps = []
        for component, conc in self.components:
            comps += [
                {
                    "x": component.get_x(),
                    "z": component.get_z(),
                    "w": component.get_w(),
                    "conc": conc,
                    "k": component.get_k(conc),
                }
            ]
        return comps



@api_view(['POST',])
def calculate_safety_klass_view(request):

    data_in_serializer = WasteSerializer(data=request.data)
    data = {}
    if data_in_serializer.is_valid():
        for objkt in request.data['components']:
            # Умножаем концентрацию на 1е4 чтобы концентрация была соизмерима
            data[objkt['id']] = objkt['concentration']*1e4
        waste = Waste(data)
        resp = {}
        resp['K'] = waste.get_summ_K()
        resp['sclass'] = waste.get_safety_class()
        resp['components'] = waste.get_components()
        return Response(resp)
    return Response(data_in_serializer.errors)
   
""" 
 let components = this.props.components.map((comp) => {
      return { id_val: comp.id, concentrat: parseFloat(comp.concentration) };
    });
 {
    "name": "dsa",
    "fkko": "Хрю хрю",
    "components": [
        {"id": 4, "concentration": 50 },
        {"id": 5, "concentration": 30 }        
        ]
}   
     """