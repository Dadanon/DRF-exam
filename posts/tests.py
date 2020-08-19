from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class PostTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1',
            password='qwe123',
        )
        testuser1.save()

        testpost1 = Post.objects.create(
            author=testuser1,
            title='One',
            body='What a body',
        )
        testpost1.save()

    def test_post_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'One')
        self.assertEqual(body, 'What a body')
