from rest_framework.viewsets import ModelViewSet
from orders.serializers import OrdersSerializer, OrderItemsSerializer
from orders.models import Orders, OrderItems
from rest_framework import permissions

from rest_framework.authentication import SessionAuthentication,TokenAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class OrdersViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (CsrfExemptSessionAuthentication, TokenAuthentication)


class OrderItemsViewSet(ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (CsrfExemptSessionAuthentication, TokenAuthentication)
