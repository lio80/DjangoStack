from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import NotRegistered

User = get_user_model()

class UserAdmin(UserAdmin):
    list_display = (
    'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')

try:
    admin.site.unregister(User)
except NotRegistered:
    pass  # It's fine if it's not registered yet
admin.site.register(User, UserAdmin)