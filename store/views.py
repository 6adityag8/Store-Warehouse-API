from rest_framework.generics import UpdateAPIView, get_object_or_404

from .models import StoreOrder
from .serializers import StoreOrderUpdateSerializer


class StoreUpdateView(UpdateAPIView):
    serializer_class = StoreOrderUpdateSerializer
    queryset = StoreOrder.objects.all()

    def get_object(self):
        return get_object_or_404(StoreOrder.objects, order_number=self.kwargs['order_number'])
