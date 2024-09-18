from django.contrib import admin
from .models import UserDefault, Tutor

class UserDefaultAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'phone_number', 'last_login')
    search_fields = ('user_name', 'email')

admin.site.register(UserDefault, UserDefaultAdmin)

class TutorAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'rating', 'verified', 'price', 'created_at')
    search_fields = ('user_name', 'email', 'services')
    list_filter = ('verified', 'availability')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Tutor, TutorAdmin)
