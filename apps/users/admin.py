from django.contrib import admin

from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone_number']


admin.site.register(User)
