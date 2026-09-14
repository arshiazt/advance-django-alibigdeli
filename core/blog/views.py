from django.shortcuts import render,get_object_or_404
from django.views.generic.base import TemplateView,RedirectView
from .models import Post

# Create your views here.

def index_view(request):
    context = {'name':'arshia'}
    return render(request,'index.html',context)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'arshiazt'
        context['posts'] = Post.objects.all()
        return context
    
class RedirectToMaktabkhone(RedirectView):
    url = 'https://maktabkhooneh.org/'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post,pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)