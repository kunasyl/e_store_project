from rest_framework import serializers

from . import models
from .services import OrderServices


class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.OrderItem
        fields = ('id', 'order_id', 'product_id', 'product_count', 'product_price')

    def create(self, validated_data):
        """
        Save order data with included order items.
        """
        order_item_data = validated_data.pop('sum_price')
        order_item = models.OrderItem.objects.create(**order_item_data)

        return order_item


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    order_items = OrderItemSerializer(many=True)
    total_price = serializers.IntegerField(min_value=0, read_only=True)
    total_sum = serializers.SerializerMethodField('count_total_price')

    class Meta:
        model = models.Order
        fields = ('id', 'user_id', 'status', 'order_items', 'total_price', 'total_sum')

    def create(self, validated_data):
        """
        Save order data with included order items.
        """
        order_items_data = validated_data.pop('order_items')
        order = models.Order.objects.create(**validated_data)
        for order_item_data in order_items_data:
            order_item_data.pop('order_id', None)
            models.OrderItem.objects.create(order_id=order, **order_item_data)

        return order

    def count_total_price(self, obj):
        """
        Calculates total sum of the order items price.
        """
        services = OrderServices()

        total_sum = 0
        for order_item in obj.order_items.all():
            total_sum += order_item.product_price * order_item.product_count
        obj.total_price = services.count_price_with_bonus(total_sum)
        obj.save()

        return total_sum

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.user_id = validated_data.get('id', instance.user_id)
        instance.status = validated_data.get('id', instance.status)
        instance.total_price = validated_data.get('id', instance.total_price)
        instance.save()
        order_items = validated_data.get('order_items')

        for order_item in order_items:
            order_item_instance = models.OrderItem.objects.get(
                order_id=order_item.get('order_id'),
                product_id=order_item.get('product_id')
            )
            print('instance', order_item_instance)
            order_item_instance.order_id = order_item.get('order_id', order_item_instance.order_id)
            order_item_instance.product_id = order_item.get('product_id', order_item_instance.product_id)
            order_item_instance.product_price = order_item.get('product_price', order_item_instance.product_price)
            order_item_instance.product_count = order_item.get('product_count', order_item_instance.product_count)
            order_item_instance.save()
        return instance
