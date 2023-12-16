from typing import Protocol, OrderedDict

from rest_framework.generics import get_object_or_404

from . import models
from .models import Cart


class UserReposInterface(Protocol):

    def create_user(self, data: OrderedDict) -> models.User: ...

    def get_user(self, data: OrderedDict): ...

    def create_cart(self, user_id) -> Cart: ...


class UserReposV1:
    model = models.User
    cart = Cart

    def create_user(self, data: OrderedDict) -> models.User:
        return self.model.objects.create_user(**data)

    def create_cart(self, user_id) -> Cart:
        return self.cart.objects.create(user_id=user_id)

    def get_user(self, data: OrderedDict):
        user = get_object_or_404(self.model, email=data['email'])

        if not user.check_password(data['password']):
            raise self.model.DoesNotExist

        return user
