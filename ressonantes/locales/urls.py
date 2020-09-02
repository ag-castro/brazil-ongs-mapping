from django.urls import path
from locales.views import CityListView, UfListView


app_name = 'locales'


urlpatterns = [
    path('ufs/', UfListView.as_view(), name='ufs'),
    path('cities/<int:uf>', CityListView.as_view(), name='cities'),
]
