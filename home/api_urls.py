
from django.urls import path, include
# from django.contrib.auth.models import User
from rest_framework import routers
from .api_views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('', include(router.urls)),
    path("products/<int:pk>", ProductDetail.as_view(), name='product_filter'),

]