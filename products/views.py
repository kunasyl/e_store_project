from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from utils import mixins
from . import serializers, models


class ProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.RetrieveProductSerializer,
    }

    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        wrapped_data = {'products': serializer.data}

        return Response(wrapped_data)

