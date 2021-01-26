import requests
from django.contrib import admin
from rest_framework.reverse import reverse

from .models import WarehouseOrder


@admin.register(WarehouseOrder)
class WarehouseOrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number',)

    def has_add_permission(self, request, obj=None):
        """
        Warehouse Orders can only be added via Store Order creation.
        """
        return False

    def save_model(self, request, obj, form, change):
        """
        Calls the endpoint to update the status of store order if status was changed.
        """
        if 'status' in form.changed_data:
            data = {
                'status': obj.status,
            }
            # TODO: error handling and retry mechanism can be implemented here
            requests.patch(reverse('update_store',
                                   kwargs={'order_number': obj.order_number},
                                   request=request), data=data)

        super(WarehouseOrderAdmin, self).save_model(request, obj, form, change)
