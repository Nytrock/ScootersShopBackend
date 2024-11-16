from django.urls import re_path, include
from rest_framework import routers
from .views import ScooterList, ScooterDetail, ScooterBuy

app_name = 'catalog'

router = routers.DefaultRouter()
router.register('buy', ScooterBuy, basename='scooter-buy')
router.register('', ScooterList, basename='scooter-list')
router.register('', ScooterDetail, basename='scooter-detail')


urlpatterns = [
    re_path('', include(router.urls)),
]