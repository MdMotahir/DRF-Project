from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from account.serializers import RegisterSerializer, UserLoginSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class RegisterApiView(APIView):
    renderer_classes=[TemplateHTMLRenderer]
    template_name = 'register.html'
    def post(self,request, *args, **kwargs):
        user_ser_obj=RegisterSerializer(data=request.data)
        if user_ser_obj.is_valid():
            user_ser_obj.save()
            return Response(user_ser_obj.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    renderer_classes=[TemplateHTMLRenderer]
    template_name = 'login.html'

    def post(self,request, *args, **kwargs):
        data_ser_obj=UserLoginSerializer(data= request.data)
        if data_ser_obj.is_valid(raise_exception=True):
            return Response(data_ser_obj.data,status=status.HTTP_200_OK)
        else:
            return Response(data_ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)