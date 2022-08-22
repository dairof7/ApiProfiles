from rest_framework import serializers, pagination
from .models import *

class TestSerializer(serializers.Serializer):
    name = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        # exclude = ('created', 'updated')

class UserSerializerComplete(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'username', 'password')
        # exclude = ('created', 'updated')
        extra_kwargs ={
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
        # def create(self, validated_data):
        #     user = UserProfile.objects.create(
        #         email=validated_data('email'),
        #         password=validated_data('password'),
        #         username=validated_data('username'),
        #     )
        #     return user
        # def update(self, instance, validated_data):
        #     print('hola########################################################')
        #     if 'password' in validated_data:
        #         password = validated_data('password')
        #         instance.set_password(password)
        #     return super().update(instance, validated_data)
