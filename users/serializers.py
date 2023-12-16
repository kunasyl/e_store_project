from rest_framework import serializers

from .models import User, Cart


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')


class CreateTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class GetUserSerializer(serializers.Serializer):
    token = serializers.CharField()

class CartSerializer(serializers.Serializer):
    class Meta:
        model = Cart
        fields = ()