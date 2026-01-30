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
        def create(self, validated_data):
            validated_data['status'] = OrderStatus.CREATED
            return super().create(validated_data)
    
        def validate_status(self, value):

            #Criação do pedido sempre em CREATED
            if not self.instance:
                return value
            
            current_status = self.instance.status

            allowed_transitions = {
                OrderStatus.CREATED: [
                    OrderStatus.PROCESSING,
                    OrderStatus.CANCELED,
                ],

                OrderStatus.PROCESSING: [
                    OrderStatus.COMPLETED,
                    OrderStatus.CANCELED,
                ],

                OrderStatus.COMPLETED: [],

                OrderStatus.CANCELED: [],
            }

            if value not in allowed_transitions[current_status]:
                raise serializers.ValidationError(
                    f"Não é possível alterar o status de {current_status} para {value}."
                )
            
            return value
        
 