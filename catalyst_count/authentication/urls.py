from django.urls import path, include


urlpatterns = [
    path('',include('allauth.urls')), #inbuilt allauth ka use kar rahe hai jissey inbuilt saarey url mil jayengey 
]
    