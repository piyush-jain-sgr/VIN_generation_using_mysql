from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="vin-home"),
    path('creatVIN/',views.creatVIN, name="create-VIN"),
    path('getVIN/',views.getVIN),
    path('openvalidateVIN/',views.openvalidateVIN,name="openvalidate-VIN"),
    path('isvalidVIN/',views.isvalidVIN),
    path('openretrieveVIN/',views.openretrieveVIN, name="openretrieve-VIN"),
    path('retrieveVIN/',views.retrieveVIN),
    path('openintervalVIN/',views.openintervalVIN,name="openinterval-VIN"),
    path('showVIN/',views.showVIN)
]