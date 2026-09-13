from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post-image/',blank=True,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Category(models.Model):

    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name