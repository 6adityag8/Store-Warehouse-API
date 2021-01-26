from django.urls import path

from .views import WarehouseCreateView, WarehouseUpdateDeleteView

urlpatterns = [
    path('api/add_warehouse',
         WarehouseCreateView.as_view(),
         name='add_warehouse'),
    path('api/update_warehouse/<slug:order_number>/',
         WarehouseUpdateDeleteView.as_view(),
         name='update_warehouse'),
]
