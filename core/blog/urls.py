from django.urls import path,include
from .views import *
from django.views.generic import TemplateView,RedirectView

app_name = 'blog'

urlpatterns = [
    path('post/api/',PostListApiView.as_view(),name='api-post-list'),
    path('fbv-index/', index_view,name='fbv-index'),
    path('cbv-index/', TemplateView.as_view(template_name='index.html',extra_context={'name':'ali'}),name='cbv-index'),
    path('cbv-view-index/', IndexView.as_view(),name='cbv-view-index'),
    path('go-to-maktabkhone/', RedirectView.as_view(url='https://maktabkhooneh.org/'),name='maktabkhone'),
    path('go-to-maktabkhone-view/', RedirectToMaktabkhone.as_view(),name='view-maktabkhone'),
    path('post/',PostListView.as_view(),name='post-list'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/form-create/',PostFormCreateView.as_view(),name='post-form-create'),
    path('post/create/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/edit/',PostEditView.as_view(),name='post-edit'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('api/v1/',include('blog.api.v1.urls')),
]