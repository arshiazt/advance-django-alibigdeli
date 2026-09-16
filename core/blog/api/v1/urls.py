from django.urls import path
from .views import *

app_name = 'api-v1'

urlpatterns = [
    path('fbv-post/',post_list,name='fbv-post-list'),
    path('fbv-post/<int:id>/',post_detail,name='fbv-post-detail'),
    path('apiview-post/',PostListApiView.as_view(),name='apiview-post-list'),
    path('apiview-post/<int:id>/',PostDetailApiView.as_view(),name='apiview-post-detail'),
    path('genericapiview-post/',PostListGenericApiView.as_view(),name='genericapiview-post-list'),
    path('genericapiview-post/<int:id>/',PostDetailGenericAPIView.as_view(),name='genericapiview-post-detail'),
    path('listcreatemixin-post/',PostListCreateMixin.as_view(),name='listcreatemixin-post-list'),
    path('listcreatemixin-post/<int:id>/',PostDetailMixin.as_view(),name='listcreatemixin-post-detail'),
    path('listcreateapiview-post/',PostListCreateApiView.as_view(),name='listcreateapiview-post-list'),
    path('listcreateapiview-post/<int:id>/',PostDetailRetrieveUpdateDestroyAPIView.as_view(),name='listcreateapiview-post-detail'),
]