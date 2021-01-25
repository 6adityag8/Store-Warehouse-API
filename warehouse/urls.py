from django.urls import path

from .views import add_warehouse

urlpatterns = [
    path('api/add_warehouse', add_warehouse, name='add_warehouse'),
]
