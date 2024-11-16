from django.contrib import admin
from django.template.defaultfilters import truncatechars

from scooters.models import Scooter


@admin.register(Scooter)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'short_description')

    def short_description(self, obj):
        return truncatechars(obj.description, 35)
    short_description.short_description = 'Описание'
