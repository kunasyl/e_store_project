import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from products.models import Product
from . import choices


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_orders',
        verbose_name=_('Пользователь')
    )
    status = models.CharField(
        choices=choices.OrderStatuses.choices,
        default=choices.OrderStatuses.NotOrdered,
        max_length=100,
        verbose_name=_('Статус заказа')
    )
    total_price = models.PositiveIntegerField(default=0, verbose_name=_('Сумма заказа'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')


class OrderItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    order_id = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        related_name='order_items',
        verbose_name=_('Заказ')
    )
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_orders',
        verbose_name=_('Товар')
    )
    product_price = models.PositiveIntegerField(default=0)
    product_count = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Товар заказа')
        verbose_name_plural = _('Товары заказа')




