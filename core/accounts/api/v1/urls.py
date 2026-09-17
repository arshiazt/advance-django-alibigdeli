from django.urls import path,include
from .views import *

app_name = 'api-v1'

urlpatterns = [
    path('registration/',RegisterApiView.as_view(),name='registration'),
    path('token/login/',CustomObtainAuthToken.as_view(),name='token-login'),
]