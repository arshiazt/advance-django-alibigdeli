from django.test import SimpleTestCase,TestCase
from datetime import datetime

from ..forms import PostForm
from ..models import Category

class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):
        cat_object = Category.objects.create(name='hello')
        form = PostForm(data={
            'title':'test',
            'content':'test1234',
            'status':True,
            'category':cat_object,
            'published_date':datetime.now()
        })
        self.assertTrue(form.is_valid())

    def test_post_form_with_invalid_data(self):
        
        form = PostForm(data={})
        self.assertFalse(form.is_valid())