from django.urls import path,include
from .views import *

urlpatterns = [
    path('registration/',RegisterApiView.as_view(),name='registration'),
]