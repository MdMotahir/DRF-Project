from django import template
from django.http import response
from django.template.response import TemplateResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from Storage.serializers import FileCrudeSerializer, FileSerializer
from django.shortcuts import redirect, render
from Storage.models import File
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from Storage.permissions import IsOwner
# Create your views here.
from rest_framework.renderers import HTMLFormRenderer, TemplateHTMLRenderer


class FileListAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name= 'Home.html'
    permission_classes=[AllowAny]

    def get(self, request):
        queryset=File.objects.all()
        return Response({'files': queryset})

class FileDetailsAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Details.html'
    lookup_field = 'slug'
    permission_classes=[IsOwner]

    def get(self, request, slug):
        file=get_object_or_404(File,slug=slug)
        serializer=FileSerializer(file)
        return Response({'file': file})

    

class FileCreateAPIView(CreateAPIView):
    renderer_classes=[TemplateHTMLRenderer]
    template_name = 'Create.html'
    queryset=File.objects.all()
    serializer_class=FileCrudeSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileUpdateAPIView(RetrieveUpdateAPIView):
    renderer_classes=[TemplateHTMLRenderer]
    template_name = 'Update.html'
    queryset=File.objects.all()
    serializer_class=FileCrudeSerializer
    lookup_field = 'slug'
    permission_classes=[IsOwner]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class FileDeleteAPIView(DestroyAPIView):
    queryset=File.objects.all()
    serializer_class=FileSerializer
    lookup_field = 'slug'
    permission_classes=[IsOwner]

