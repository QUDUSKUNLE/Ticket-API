import json

from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User

client = APIClient()


class CategoryTestCase(TestCase):

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
        self.url = '/api/categories/'

    def test_create_category(self):
        """
        Test create a new category
        """
        data = dict(
            name='Premium',
            slug='CreditCard'
        )
        response = client.post(
            self.url,
            data=data,
            HTTP_AUTHORIZATION="Bearer {}".format(self.access),
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.content)['name'], 'Premium')
        self.assertEqual(json.loads(response.content)['slug'], 'CreditCard')

    def test_category_list(self):
        """
        Ensure we can view list of categories.
        """
        response = client.get(self.url, format='json')
        self.assertEqual(type(json.loads(response.content)['results']), list)
        self.assertEqual(response.status_code, 200)
