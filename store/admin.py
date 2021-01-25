import requests
from django.contrib import admin
from rest_framework import status
from rest_framework.reverse import reverse

from .models import StoreOrder


@admin.register(StoreOrder)
class StoreOrderAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        data = {
            'status': obj.status,
            'order_number': obj.order_number,
        }
        response = requests.post(reverse('add_warehouse', request=request), data=data)
        if int(response.status_code) == status.HTTP_201_CREATED:
            super().save_model(request, obj, form, change)
