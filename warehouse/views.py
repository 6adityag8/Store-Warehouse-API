from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404, CreateAPIView

from .models import WarehouseOrder
from .serializers import WarehouseOrderSerializer


class WarehouseCreateView(CreateAPIView):
    """
    Creates a new Warehouse Order.
    """
    serializer_class = WarehouseOrderSerializer


class WarehouseUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Updates the warehouse order if method is PATCH
    and deletes the order if method is DELETE.
    """
    serializer_class = WarehouseOrderSerializer
    queryset = WarehouseOrder.objects.all()

    def get_object(self):
        return get_object_or_404(WarehouseOrder.objects, order_number=self.kwargs['order_number'])
