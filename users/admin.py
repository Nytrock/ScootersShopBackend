from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import Customer, Purchase


class UserProfileInlined(admin.StackedInline):
    model = Customer
    can_delete = False
    min_num = 1
    max_num = 1
    extra = 1

    list_display = ('balance', )


class CustomerAdmin(UserAdmin):
    inlines = (UserProfileInlined,)


@admin.register(Purchase)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'scooter', 'buy_time')


admin.site.unregister(User)
admin.site.register(User, CustomerAdmin)
