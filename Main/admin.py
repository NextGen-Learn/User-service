from django.contrib import admin
from .models import UserDefault, Tutor

class UserDefaultAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'phone_number', 'last_login')
    search_fields = ('user_name', 'email')
    list_filter = ('last_login',)
    ordering = ('-last_login',)
    
    fieldsets = (
        (None, {
            'fields': ('user_name', 'email', 'phone_number')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('last_login',)
        }),
    )

    actions = ['send_email']

    def send_email(self, request, queryset):
        self.message_user(request, "Email has been sent successfully to selected users.")
    send_email.short_description = "Send email to selected users"

admin.site.register(UserDefault, UserDefaultAdmin)

class TutorAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'rating', 'verified', 'price', 'created_at')
    search_fields = ('user_name', 'email', 'services')
    list_filter = ('verified', 'availability', 'rating')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('user_name', 'email', 'price')
        }),
        ('Ratings and Verification', {
            'fields': ('rating', 'verified', 'availability')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Tutor, TutorAdmin)
