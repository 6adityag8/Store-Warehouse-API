from django.contrib import admin
from django.urls import path, include

from store import urls as store_url
from warehouse import urls as warehouse_url

urlpatterns = [
    path('', admin.site.urls),
    path('store/', include(store_url)),
    path('warehouse/', include(warehouse_url)),
]
