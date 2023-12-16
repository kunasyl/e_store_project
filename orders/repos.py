from . import models


class OrderRepos:
    model = models.Order

    def get_user_orders(self, user):
        return self.model.objects.filter(user_id=user)

    def get_orders(self):
        return self.model.objects.all()

    def get_order(self, pk):
        return self.model.objects.get(id=pk)
