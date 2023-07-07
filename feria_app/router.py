from rest_framework import routers
from .viewsets import ProductoViewSet

router = routers.SimpleRouter()
router.register("api_producto",ProductoViewSet) 