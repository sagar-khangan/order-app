from rest_framework.serializers import ModelSerializer
from orders.models import Orders, OrderItems


class OrdersSerializer(ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'


class OrderItemsSerializer(ModelSerializer):

    class Meta:
        model = OrderItems
        fields = '__all__'
