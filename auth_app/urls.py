from django.urls import path
from .views import test_api
from .views import register_view
from .views import custom_token


urlpatterns = [
    path('test/', test_api, name='test_api'),
    path('register/', register_view, name='register'),
    path('login/', custom_token, name='login')
]