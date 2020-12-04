from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.fields import CharField, EmailField






class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username','email','first_name','last_name','password')
        extra_kwargs={'password':{'write_only': True}}
    
    def create(self, validated_data):
        user=get_user_model().objects.create_user(validated_data['username'],
        email=validated_data['email'], password=validated_data['password'],
        first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= get_user_model()
        fields = ('username','email','first_name','last_name',)


class UserLoginSerializer(serializers.ModelSerializer):
    token=CharField(allow_blank=True, read_only=True)
    username=CharField()
    email=EmailField()
    class Meta:
        model = get_user_model()
        fields = ('username','email','password','token',)
        extra_kwargs={'password':{'write_only': True}}
    
    def validate(self, data):
        return data