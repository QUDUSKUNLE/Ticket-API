from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from tickets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/tickets', views.TicketViewSet)
router.register(r'api/categories', views.CategoryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]
