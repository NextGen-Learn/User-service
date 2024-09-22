from rest_framework import serializers
from .models import UserDefault, Tutor

class UserDefaultSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserDefault
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserDefault(**validated_data)
        user.set_password(password)
        user.save()
        return user

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'