import json

from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User

client = APIClient()


class UserTestCase(TestCase):

    def setUp(self):
        """
        Ensure we can create superuser
        """
        new_user = User.objects.create_superuser(
            username="test1",
            email='test@gmailcom',
            password='test08971'
        )
        users_count_before = User.objects.count()
        data = dict(
            username='test1',
            password='test08971'
        )
        response = client.post('/api/token/', data=data, format='json')
        self.users_count_before = users_count_before
        self.superuser = new_user
        self.access = (json.loads(response.content))['access']
        self.url = '/api/users/'

    def test_superuser(self):
        """
        Test that super user is created
        """
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)

    def test_add_user(self):
        """
        Test for adding more user
        """
        new_user = User.objects.create(
            username='test2',
            email='test2@gmail.com',
            password='test208971'
        )
        users_count_after = User.objects.count()
        self.assertFalse(new_user.is_staff)
        self.assertEqual(self.users_count_before + 1, users_count_after)

    def test_user_list(self):
        """
        Ensure we can view list of users.
        """
        response = client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)
