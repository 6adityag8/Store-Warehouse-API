from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework.test import APITestCase

from .models import StoreOrder
from .views import StoreUpdateView


class TestUrls(SimpleTestCase):

    def test_update_store_url_resolves(self):
        url = reverse('update_store', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, StoreUpdateView)


class TestViews(APITestCase):
    databases = '__all__'

    def test_update_warehouse(self):
        sample_store_order_number = 'sample_order_number'
        StoreOrder.objects.create(status='0', order_number=sample_store_order_number)
        initial_store_count = StoreOrder.objects.count()
        new_status = '1'
        self.client.patch(reverse('update_store', args=[sample_store_order_number]), data={'status': new_status})

        self.assertEqual(StoreOrder.objects.count(), initial_store_count)

        self.assertEqual(StoreOrder.objects.get(order_number=sample_store_order_number).status, new_status)
