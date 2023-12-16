import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from . import choices
from users.models import User


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'), unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Цена'))
    description = models.TextField(verbose_name=_('Описание'))
    category = models.CharField(
        choices=choices.ProductChoices.choices,
        null=True,
        blank=True,
        max_length=100,
        verbose_name=_('Категория')
    )
    # Главное изображение
    product_image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение товара')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, verbose_name=_('Рейтинг'))
    rating_count = models.IntegerField(default=0, verbose_name=_('Количество обзоров'))
    sale = models.FloatField(null=True, blank=True, verbose_name=_('Процент скидки'))
    product_count = models.IntegerField(verbose_name=_('Количество товаров'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        
        
class ProductImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_images',
        verbose_name=_('Товар')
    )
    image = models.ImageField(upload_to='products_images/%Y/%m/%d', verbose_name=_('Изображение'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Изображение товара')
        verbose_name_plural = _('Изображения товара')


class ProductReview(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='product_reviews',
        verbose_name=_('Отзыв о товары')
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_reviews',
        verbose_name=_('Товар')
    )
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name=_('Отзыв'))
    review_text = models.TextField(verbose_name=_('Отзыв'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Отзыв о товаре')
        verbose_name_plural = _('Отзывы о товаре')
