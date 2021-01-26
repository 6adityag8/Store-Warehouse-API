from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework.test import APITestCase

from .models import WarehouseOrder
from .views import WarehouseCreateView, WarehouseUpdateDeleteView


class TestUrls(SimpleTestCase):

    def test_add_warehouse_url_resolves(self):
        url = reverse('add_warehouse')

        self.assertEquals(resolve(url).func.view_class, WarehouseCreateView)

    def test_update_warehouse_url_resolves(self):
        url = reverse('update_warehouse', args=['some-slug'])

        self.assertEquals(resolve(url).func.view_class, WarehouseUpdateDeleteView)


class TestViews(APITestCase):
    databases = '__all__'
    sample_warehouse_order_number = 'sample_order_number'

    def test_create_warehouse(self):
        initial_warehouse_count = WarehouseOrder.objects.count()
        warehouse_attrs = {
            'status': '0',
            'order_number': 'a_valid_order_number',
        }
        response = self.client.post(reverse('add_warehouse'), warehouse_attrs)

        self.assertEqual(WarehouseOrder.objects.count(), initial_warehouse_count + 1)

        for attr, expected in warehouse_attrs.items():
            self.assertEqual(response.data[attr], expected)

    def test_delete_warehouse(self):
        WarehouseOrder.objects.create(status='0', order_number=self.sample_warehouse_order_number)
        initial_warehouse_count = WarehouseOrder.objects.count()
        self.client.delete(reverse('update_warehouse', args=[self.sample_warehouse_order_number]))

        self.assertEqual(WarehouseOrder.objects.count(), initial_warehouse_count - 1)

        self.assertRaises(
            WarehouseOrder.DoesNotExist,
            WarehouseOrder.objects.get,
            order_number=self.sample_warehouse_order_number
        )

    def test_update_warehouse(self):
        WarehouseOrder.objects.create(status='0', order_number=self.sample_warehouse_order_number)
        initial_warehouse_count = WarehouseOrder.objects.count()
        new_status = '1'
        self.client.patch(reverse('update_warehouse', args=[self.sample_warehouse_order_number]),
                          data={'status': new_status})

        self.assertEqual(WarehouseOrder.objects.count(), initial_warehouse_count)

        self.assertEqual(WarehouseOrder.objects.get(order_number=self.sample_warehouse_order_number).status, new_status)
