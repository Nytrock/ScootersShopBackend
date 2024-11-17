from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('users/', include('users.urls')),
    path('scooters/', include('scooters.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)