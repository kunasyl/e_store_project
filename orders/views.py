from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

from . import models, serializers, services, permissions


class OrderView(APIView):
    order = models.Order
    services = services.OrderServices()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        return permissions.IsOrderUser(),

    def get(self, request, *args, **kwargs):
        # query orders of the current authorized user
        orders = self.services.get_user_orders(request.user)
        serializer = serializers.OrderSerializer(orders, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.OrderSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            valid_serializer = serializer.save()

            return Response({"success": "Order '{}' created successfully".format(valid_serializer.id)})

        return Response(serializer.errors)

    def put(self, request):
        order = self.services.get_order(pk=request.data.get('id'))
        serializer = serializers.OrderSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
