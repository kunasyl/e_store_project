# Generated by Django 4.1.7 on 2023-05-06 15:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ('-created_at',), 'verbose_name': 'Изображение товара', 'verbose_name_plural': 'Изображения товара'},
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Отзыв')),
                ('review_text', models.TextField(verbose_name='Отзыв')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to=settings.AUTH_USER_MODEL, verbose_name='Отзыв о товары')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Отзыв о товаре',
                'verbose_name_plural': 'Отзывы о товаре',
                'ordering': ('-created_at',),
            },
        ),
    ]
