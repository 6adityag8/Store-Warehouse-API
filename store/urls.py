from django.urls import path

from .views import update_store

urlpatterns = [
    path('api/update_store', update_store, name='update_store'),
]
