from django.db import models

from store_warehouse_api.constants import STATUS_CHOICES


class StoreOrder(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')

    def __str__(self):
        return 'Store Order: {0}'.format(str(self.order_number))
