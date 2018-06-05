from django.contrib import admin

# Register your models here.

from .models import Ticket, Category

admin.site.register(Ticket)
admin.site.register(Category)
