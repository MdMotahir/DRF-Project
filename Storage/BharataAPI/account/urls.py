from django.urls import path,include
from account.views import RegisterApiView, UserLoginAPIView



urlpatterns = [
    path('register',RegisterApiView.as_view(),name='register'),
    path('login',UserLoginAPIView.as_view(),name='login'),
]