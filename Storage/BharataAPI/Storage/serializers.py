from rest_framework.fields import SerializerMethodField
from account.serializers import UserSerializer
from django.db.models import fields
from rest_framework import serializers
from Storage.models import File


class FileCrudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('name','author','type','file',)


File_Url=serializers.HyperlinkedIdentityField(
    view_name='details',
    lookup_field='slug',
)



class FileSerializer(serializers.ModelSerializer):
    url=File_Url
    author=UserSerializer(read_only=True)
    class Meta:
        model = File
        fields=('url','id','name','author','type','file','slug',)
