from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Entry


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username="testuser1", password="abc123")
        testuser1.save()

        # Create a blog post
        test_post = Entry.objects.create(
            author=testuser1, title="Blog title", body="Body content..."
        )
        test_post.save()

    def test_blog_content(self):
        entry = Entry.objects.get(id=1)
        expected_author = f"{entry.author}"
        expected_title = f"{entry.title}"
        expected_body = f"{entry.body}"
        self.assertEqual(expected_author, "testuser1")
        self.assertEqual(expected_title, "Blog title")
        self.assertEqual(expected_body, "Body content...")


class PostModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_post = Entry.objects.create(
            author=test_user, title="Title of Blog", body="Words about the blog"
        )
        test_post.save()

    def test_blog_content(self):
        entry = Entry.objects.get(id=1)

        self.assertEqual(str(entry.author), "tester")
        self.assertEqual(entry.title, "Title of Blog")
        self.assertEqual(entry.body, "Words about the blog")
