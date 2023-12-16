from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

# router = DefaultRouter()
# router.register(r'', OrderViewSet.as_view({'get':'list'}), basename='orders')
urlpatterns = [
    path('', OrderView.as_view())
]
