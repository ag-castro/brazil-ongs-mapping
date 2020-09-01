from django.test import TestCase
from core.models import City, Uf


payload_uf = {
    'acronym': 'GO',
    'name': 'Goiás',
    'region': 'Centro-Oeste',
}


class LocalesModelsTest(TestCase):

    def test_create_uf_successful(self):
        """Test creating new UF locale successful"""

        uf_obj = Uf.objects.create(
            acronym=payload_uf['acronym'],
            name=payload_uf['name'],
            region=payload_uf['region']
        )

        self.assertEqual(uf_obj.acronym, payload_uf['acronym'])
        self.assertEqual(uf_obj.name, payload_uf['name'])
        self.assertEqual(uf_obj.region, payload_uf['region'])

    def test_uf_str(self):
        """Test the UF string representation"""
        uf = Uf.objects.create(
            acronym=payload_uf['acronym'],
            name=payload_uf['name'],
            region=payload_uf['region']
        )
        self.assertEqual(str(uf), uf.name)

    def test_create_city_successful(self):
        """Test creating new City locale successful"""
        uf_obj = Uf.objects.create(
            acronym=payload_uf['acronym'],
            name=payload_uf['name'],
            region=payload_uf['region']
        )
        city_obj = City.objects.create(
            uf=uf_obj,
            name='Goiânia'
        )
        self.assertEqual(uf_obj, city_obj.uf)

    def test_city_str(self):
        """Test the City string representation"""

        uf_obj = Uf.objects.create(
            acronym=payload_uf['acronym'],
            name=payload_uf['name'],
            region=payload_uf['region']
        )
        city_obj = City.objects.create(
            uf=uf_obj,
            name='Goiânia'
        )
        self.assertEqual(str(city_obj), city_obj.name)
