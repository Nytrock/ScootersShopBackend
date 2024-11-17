from django.urls import path

from scooters.views import ScooterListView, ScooterDetailView

app_name = 'catalog'
urlpatterns = [
    path("<int:id>", ScooterDetailView.as_view(), name='scooter_detail'),
    path("", ScooterListView.as_view(), name='scooters'),
]