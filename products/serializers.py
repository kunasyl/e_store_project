from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Product
        fields = ('id', 'title', 'price', 'product_image',
                  'rating', 'rating_count', 'sale')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ('image', )


# Serializer for product details
class RetrieveProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    product_images = ProductImageSerializer(many=True)

    class Meta:
        model = models.Product
        fields = ('id', 'title', 'price', 'description', 'category', 'product_image',
                  'rating', 'rating_count', 'sale', 'product_count', 'product_images')

    def create(self, validated_data):
        images_data = validated_data.pop('product_images')
        product = models.Product.objects.create(**validated_data)
        for image_data in images_data:
            models.ProductImage.objects.create(product=product, **image_data)
        return product
