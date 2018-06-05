from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from tickets.models import Ticket, Category, generate_ticket_id

class CategoryTest(TestCase):

    def create_category(self, name='Python', slug='www.python.org'):
        return Category.objects.create(name=name, slug=slug)

    def test_category_creation(self):
        w = self.create_category()
        self.assertTrue(isinstance(w, Category))


class TicketTest(TestCase):
    
    def create_category(self, name='Python', slug='www.python.org'):
        return Category.objects.create(name=name, slug=slug)

    def create_user(self, name='kunle', password='kunle08971', email='kunle@gmail.com'):
        return User.objects.create(username=name, password=password, email=email)
    
    def create_ticket(self):
        self.title = '2 Bedroom Flat'
        self.user = self.create_user()
        self.content = 'New Booking'
        self.category=self.create_category()
        self.ticket_id = generate_ticket_id()
        self.created = timezone.now()
        return Ticket.objects.create(title=self.title, user=self.user, content=self.content, category=self.category, ticket_id=self.ticket_id, created=self.created)

    def test_create_ticket(self):
        ticket = self.create_ticket()
        self.assertEquals(ticket.title, '2 Bedroom Flat')
        self.assertTrue(isinstance(ticket, Ticket))


class GenerateIdTest(TestCase):
    
    def test_generate_id(self):
        self.id = generate_ticket_id()
        self.assertTrue(self.id)
