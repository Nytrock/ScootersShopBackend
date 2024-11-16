from django.urls import re_path

from .views import ScooterCreate, ScooterList, ScooterDetail

app_name = 'catalog'

urlpatterns = [
    re_path('add', ScooterCreate.as_view()),
    re_path('', ScooterList.as_view()),
    re_path('<int:id>/', ScooterDetail.as_view()),
    # re_path('toCart/<int:scooter_id>/', AddToCart.as_view()),
]