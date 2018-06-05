import json

from django.contrib.auth.models import User
from tickets.models import Ticket, Category, generate_ticket_id
from tickets.urls import urlpatterns
from tickets.views import UserViewSet, TicketViewSet, CategoryViewSet
from rest_framework.test import APITestCase, URLPatternsTestCase, APIRequestFactory, force_authenticate

from django.urls import include, reverse
from django.conf.urls import url, include


class UserListView(APITestCase, URLPatternsTestCase):

    urlpatterns = [
        url(r'^', include('tickets.urls'))
    ]

    def test_user_list(self):
        """
        Ensure we can view list of users.
        """
        view = UserViewSet.as_view({'get': 'list'})
        request = APIRequestFactory().get('/api/users/', format='json')
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, 200)

class CategoryListView(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'^', include('tickets.urls'))
    ]

    def test_category_list(self):
        """
        Ensure we can view list of categories.
        """
        view = CategoryViewSet.as_view({'get': 'list'})
        request = APIRequestFactory().get('/api/categories/', format='json')
        response = view(request)
        response.render()
        self.assertEqual(type(json.loads(response.content)['results']), list)
        self.assertEqual(response.status_code, 200)
    

class TicketListView(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'^', include('tickets.urls'))
    ]

    def test_ticket_list(self):
        """
        Ensure we can view list of tickets.
        """
        view = TicketViewSet.as_view({'get': 'list'})
        request = APIRequestFactory().get('/api/tickets/', format='json')
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, 200)
