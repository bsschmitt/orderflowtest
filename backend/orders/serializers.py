from rest_framework import serializers
from .models import Order, OrderStatus

class OrderSerializer(serializers.ModelSerializer):

    def valida_status(self, value):
        valid_statuses = [status.value for status in OrderStatus]

        if value not in valid_statuses:
            raise serializers.ValidationError(
                f"Status inválido. Use um dos valores: {valid_statuses}"
            )
        
        return value
    
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
            'created_at',
            'updated_at',
        ]