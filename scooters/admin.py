from django.contrib import admin

from scooters.models import Scooter


@admin.register(Scooter)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'max_speed', 'weight', 'price')
