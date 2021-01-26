from django.db import models

from store_warehouse_api.constants import STATUS_CHOICES


class WarehouseOrder(models.Model):
    order_number = models.SlugField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')

    def get_status_text(self):
        for status in STATUS_CHOICES:
            if status[0] == self.status:
                return status[1]

    def __str__(self):
        return 'Warehouse Order: {0} - {1}'.format(str(self.order_number), self.get_status_text())
