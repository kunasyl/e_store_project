# Generated by Django 4.1.7 on 2023-05-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_bonus_alter_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='bonus',
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Сумма заказа'),
        ),
    ]
