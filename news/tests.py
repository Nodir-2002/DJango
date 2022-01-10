from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.
class PostModelTest(TestCase):
    def setup(self):
        Post.objects.create(title='Havo',text='bugun havo ochiq')

    def text_test(self):
        post=Post.objects.get(id=1)
        Ttitle =f"{post.title}"
        Ttext = f"{post.text}"
        self.assertEqual(Ttitle,'Havo')
        self.assertEqual(Ttext,'bugun havo ochiq')

