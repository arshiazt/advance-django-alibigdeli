from django.shortcuts import render,get_object_or_404
from django.views.generic.base import TemplateView,RedirectView
from .models import Post
from .forms import PostForm
from django.views.generic import ListView,DetailView,FormView,CreateView

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
    
class PostListView(ListView):
    model = Post
    # queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
    
class PostDetailView(DetailView):
    model = Post

class PostFormCreateView(FormView):
    template_name = 'blog/contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class PostCreateView(CreateView):
    model = Post
    # fields = [
    #         'author','title',
    #         'content','status',
    #         'category','published_date',
    #     ]
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)