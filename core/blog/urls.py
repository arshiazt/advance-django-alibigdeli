from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('fbv-index/', index_view,name='fbv-index'),
    path('cbv-index/', TemplateView.as_view(template_name='index.html',extra_context={'name':'ali'}),name='cbv-index'),
    path('cbv-view-index/', IndexView.as_view(),name='cbv-view-index'),
]