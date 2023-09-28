from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only':True}}

    # def create(self, validated_data):
    #     return CustomUser.objects.create_user(**validated_data)

    # Dee's fix
    def create(self, validated_data):
        user = CustomUser.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            email = validated_data['email']
        )
        user.save
        return CustomUser(**validated_data)

