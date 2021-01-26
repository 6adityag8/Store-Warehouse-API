import requests
from django.contrib import admin
from rest_framework.reverse import reverse

from .models import StoreOrder


@admin.register(StoreOrder)
class StoreOrderAdmin(admin.ModelAdmin):

    # TODO: error handling and retry mechanism can be implemented while making API calls
    def save_model(self, request, obj, form, change):
        """
        Create and update Warehouse Order upon creating and updating
        Store Order by calling create and update API endpoints.
        """
        data = {
            'status': obj.status,
            'order_number': obj.order_number,
        }
        # If change is True then update else create
        if change:
            requests.patch(reverse('update_warehouse',
                                   kwargs={'order_number': obj.order_number},
                                   request=request), data=data)
        else:
            requests.post(reverse('add_warehouse', request=request), data=data)

        super(StoreOrderAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        """
        Delete the Warehouse Order with this order number when
        Store order is deleted by calling delete API endpoint.
        """
        requests.delete(reverse('update_warehouse', kwargs={'order_number': obj.order_number}, request=request))

        super(StoreOrderAdmin, self).delete_model(request, obj)
