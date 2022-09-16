from django.test import TestCase
from litsource.models import LitSource
from .models import Substance

class TestSubstance(TestCase):

    def setUp(self):
        self.lsource = LitSource.objects.create(
            name='Гост',            
        )
        pass
        self.substance = Substance.objects.create(

        )
