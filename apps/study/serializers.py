from rest_framework import serializers
from .models import User


# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     email = serializers.CharField(required=True)
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_active', 'avatar', 'comment')