from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 70, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError('The username should be alphanumeric characters')
        return attrs
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password' ]

