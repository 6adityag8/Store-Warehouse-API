from django.urls import path

from .views import StoreUpdateView

urlpatterns = [
    path('api/update_store/<slug:order_number>',
         StoreUpdateView.as_view(),
         name='update_store'),
]
