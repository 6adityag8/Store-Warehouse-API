from django.db import models

STATUS_CHOICES = (
    ('0', 'New'),
    ('1', 'In Process'),
    ('2', 'Stored'),
    ('3', 'Send'),
)


class StoreOrder(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')

    def __str__(self):
        return str(self.order_number)
