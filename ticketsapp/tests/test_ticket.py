import json

from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User
from tickets.models import Ticket, Category

client = APIClient()


class TicketTestCase(TestCase):

    def setUp(self):
        """"
        Set up superuser
        """
        self.super_admin = User.objects.create_superuser(
            username='test3',
            password='test308971',
            email='test3@gmail.com'
        )
        data = dict(
            username='test3',
            password='test308971'
        )
        self.create_category = Category.objects.create(
            name='Premium',
            slug='CreditCard'
        )
        self.get_user = User.objects.get(
            username='test3'
        )
        self.category = Category.objects.get(
            name='Premium'
        )
        response = client.post('/api/token/', data=data, format='json')
        self.access_token = (json.loads(response.content))['access']
        self.url = '/api/tickets/'


    def test_create_ticket(self):
        """
        Test user can create ticket
        """

        self.ticket = Ticket(
            title='Python Ticket',
            user=self.get_user,
            content='The Beginning of Python',
            category=self.category
        )
        self.ticket.save()
        response = client.get(
            self.url,
            HTTP_AUTHORIZATION="Bearer {}".format(self.access_token),
            format='json'
        )
        self.assertEqual((json.loads(response.content)['results'][0]['title']),
                        'Python Ticket')
        self.assertIn(self.ticket.content,
                        json.loads(response.content)['results'][0]['content'])

    def test_ticket_list(self):
        """
        Ensure we can view list of tickets.
        """
        response = client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)
