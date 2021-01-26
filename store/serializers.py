from rest_framework import serializers

from .models import StoreOrder


class StoreOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreOrder
        fields = ('status',)
