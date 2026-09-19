from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('post',PostModelViewSet,basename='post')
router.register('category',CategoryModelViewSet,basename='category')

urlpatterns = router.urls



# urlpatterns = [
#     path('fbv-post/',post_list,name='fbv-post-list'),
#     path('fbv-post/<int:id>/',post_detail,name='fbv-post-detail'),
#     path('apiview-post/',PostListApiView.as_view(),name='apiview-post-list'),
#     path('apiview-post/<int:id>/',PostDetailApiView.as_view(),name='apiview-post-detail'),
#     path('genericapiview-post/',PostListGenericApiView.as_view(),name='genericapiview-post-list'),
#     path('genericapiview-post/<int:id>/',PostDetailGenericAPIView.as_view(),name='genericapiview-post-detail'),
#     path('listcreatemixin-post/',PostListCreateMixin.as_view(),name='listcreatemixin-post-list'),
#     path('listcreatemixin-post/<int:id>/',PostDetailMixin.as_view(),name='listcreatemixin-post-detail'),
#     path('listcreateapiview-post/',PostListCreateApiView.as_view(),name='listcreateapiview-post-list'),
#     path('listcreateapiview-post/<int:id>/',PostDetailRetrieveUpdateDestroyAPIView.as_view(),name='listcreateapiview-post-detail'),
#     path('viewset-viewset-post/',PostViewSet.as_view({'get':'list','post':'create'}),name='viewset-viewset-post-list'),
#     path('viewset-viewset-post/<int:pk>/',PostViewSet.as_view({'get':'retrive','put':'update','patch':'partial_update','delete':'destroy'}),name='viewset-viewset-post-detail'),
# ]