from rest_framework import serializers
from .models import UserDefault

class UserDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDefault
        fields = ['email', 'user_name', 'phone_number', 'avatar', 'last_login']
