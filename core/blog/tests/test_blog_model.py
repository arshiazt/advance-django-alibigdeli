from django.test import TestCase
from datetime import datetime
from accounts.models import User,Profile
from ..models import Category,Post

class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='test@test.com',
            password='a/@12345Asd'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name='arshia',
            last_name='tehrani',
            description='test',
        )

    def test_create_post_with_valid_data(self):
        
        post = Post.objects.create(
            author=self.profile,
            title='test',
            content='test1234',
            status=True,
            category=None,
            published_date=datetime.now()
        )
        
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual(post.title,'test')