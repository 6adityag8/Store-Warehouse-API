from django.contrib import admin

from .models import WarehouseOrder


@admin.register(WarehouseOrder)
class WarehouseOrderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
