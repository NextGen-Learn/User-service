from django.contrib import admin
from .models import UserDefault

class UserDefaultAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'phone_number', 'last_login')
    search_fields = ('user_name', 'email')

admin.site.register(UserDefault, UserDefaultAdmin)
