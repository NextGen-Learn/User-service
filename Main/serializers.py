from rest_framework import serializers
from .models import UserDefault, Tutor

class UserDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDefault
        fields = ['email', 'user_name', 'phone_number', 'avatar', 'last_login']

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'