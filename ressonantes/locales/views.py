from rest_framework.generics import ListAPIView
from core.models import City, Uf
from locales.serializers import CitySerializer, UfSerializer


class UfListView(ListAPIView):
    """The list view for UF model objects"""

    serializer_class = UfSerializer
    queryset = Uf.objects.all()


class CityListView(ListAPIView):
    """The list view for City model objects filtered by UF pk"""

    serializer_class = CitySerializer

    def get_queryset(self):
        objs = City.objects.filter(uf=self.kwargs['uf'])
        return objs
