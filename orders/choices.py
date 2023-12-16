from django.db import models


class OrderStatuses(models.TextChoices):
    NotOrdered = 'Не заказано'
    Processing = 'Заказ в обработке'
    Ordered = 'Заказано'
    Delivered = 'Получено'
    NotDelivered = 'Не получено'
