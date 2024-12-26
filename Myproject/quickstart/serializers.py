from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import serializers
from quickstart.models import UserToken

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}


    #custom validation for email uniqueness
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
        return super().update(instance, validated_data)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']



class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserToken
        fields = ['user', 'access_token', 'refresh_token']