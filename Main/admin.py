from django.contrib import admin
from .models import UserDefault, Tutor

class UserDefaultAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone_number', 'created_at', 'updated_at')  

admin.site.register(UserDefault, UserDefaultAdmin)

admin.site.register(Tutor)
