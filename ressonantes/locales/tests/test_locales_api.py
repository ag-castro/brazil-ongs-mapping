from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from core.models import City, Uf


UF_ENDPOINT = reverse('locales:ufs')
CITY_ENDPOINT = reverse('locales:cities', kwargs={'uf': 1})

payload_uf = {
    'acronym': 'GO',
    'name': 'Goiás',
    'region': 'Centro-Oeste',
}


class LocalesApiTests(TestCase):

    def test_getting_uf_list(self):
        """Test getting the Uf list objects from it's endpoint"""

        response = self.client.get(UF_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uf_methods_not_allowed(self):
        """Test UF endpoint POST, DELETE, PATCH, PUT Method NOT Allowed"""

        response = self.client.post(UF_ENDPOINT, {})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.delete(UF_ENDPOINT, {})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.patch(UF_ENDPOINT, {})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put(UF_ENDPOINT, {})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_getting_cities_list(self):
        """Test getting the City list from UF"""

        uf_obj = Uf.objects.create(**payload_uf)
        city_obj = City.objects.create(
            uf=uf_obj,
            name='Goiânia'
        )

        self.assertEqual(uf_obj, city_obj.uf)
        response = self.client.get(
            reverse('locales:cities', kwargs={'uf': uf_obj.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['uf'], uf_obj.pk)
        self.assertEqual(response.data[0]['name'], city_obj.name)

    def test_cities_methods_not_allowed(self):
        """Test Cities endpoint POST, DELETE, PATCH, PUT Method NOT Allowed"""

        response = self.client.post(CITY_ENDPOINT, {})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.delete(CITY_ENDPOINT, {})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.patch(CITY_ENDPOINT, {})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put(CITY_ENDPOINT, {})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
