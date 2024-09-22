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
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['password'] = instance.password
        return representation

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = UserDefault.objects.get(email=email)
        except UserDefault.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password.")

        attrs['user'] = user
        return attrs