from django.db import models
from django.conf import settings

#Definindo o Status dos pedidos
class OrderStatus(models.TextChoices):
    CREATED    = 'CREATED', 'Created'
    PROCESSING = 'PROCESSING', 'Processing'
    COMPLETED  = 'COMPLETED', 'Completed'
    CANCELED   = 'CANCELED', 'Canceled'

#Relacionamento dos pedidos com os usuários
class Order(models.Model):
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='orders'
    )
#Definição de status 
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.CREATED
    )
#Mostrando data de criação / atualização do pedido
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
#Ao buscar pedidos mostrar na sequencia de criação
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order #{self.id} - {self.status}'
