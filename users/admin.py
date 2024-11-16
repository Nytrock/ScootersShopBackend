from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import Customer


class UserProfileInlined(admin.StackedInline):
    model = Customer
    can_delete = False
    min_num = 1
    max_num = 1
    extra = 1


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInlined,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
