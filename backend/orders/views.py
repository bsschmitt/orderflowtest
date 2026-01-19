from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderSerializer

class ORderViewSet(ModelViewSet):
    """
    ViewSet responsável pelos endpoints de pedidos (Orders).

    Regras:
    - Apenas usuários autenticados acessam
    - Usuário só enxerga os próprios pedidos
    - Pedido criado sempre pertence ao usuário autenticado 
    """

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        #Retorna os pedidos do usuário autenticado

        return Order.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        #Associa automaticamente o pedido ao usuário autenticado 

        serializer.save(user=self.request.user)
