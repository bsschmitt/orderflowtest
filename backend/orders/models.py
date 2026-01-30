from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class OrderStatus(models.TextChoices):
    CREATED = 'CREATED', 'Created'
    PROCESSING = 'PROCESSING', 'Processing'
    COMPLETED = 'COMPLETED', 'Completed'
    CANCELED = 'CANCELED', 'Canceled'


class Order(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.CREATED,
        db_index=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order #{self.id} - {self.get_status_display()}'

    # VALIDAÇÃO CENTRAL DO DOMÍNIO
    def clean(self):

        # BLOQUEIA criação com status diferente de CREATED
        if not self.pk:
            if self.status != OrderStatus.CREATED:
                raise ValidationError(
                    "New orders must be created with status CREATED."
                )
            return

        # ---------- UPDATE ----------
        old_order = Order.objects.get(pk=self.pk)

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

        if self.status != old_order.status:
            if self.status not in allowed_transitions[old_order.status]:
                raise ValidationError(
                    f"Cannot change status from {old_order.status} to {self.status}"
                )

    # GARANTE QUE clean() SEMPRE RODE
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
