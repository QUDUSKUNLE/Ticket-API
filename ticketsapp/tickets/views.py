from django.shortcuts import render

# Create your views here.
from rest_framework import routers, serializers, viewsets
from .serializer import UserSerializer, TicketSerializer, CategorySerializer
from django.contrib.auth.models import User
from .models import Ticket, Category


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.get_queryset().order_by('id')
    serializer_class = UserSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.get_queryset().order_by('id')
    serializer_class = TicketSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.get_queryset().order_by('id')
    serializer_class = CategorySerializer
