from rest_framework import serializers
from .models import Order, OrderStatus

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'status',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]