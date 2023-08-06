from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли должны совпадать.'})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user
    
    
    
class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance
    
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' ,'username', 'email', 'first_name', 'last_name')
        
class UserDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' ,'username', 'email', 'first_name', 'last_name')
    
class UserSerializer(serializers.ModelField):
    class Meta:
        model = User
        fields = ('id' ,'username', 'email')