
from django.urls import path
from .views import ProductoListView,ProductoCreateView , ProductoDeleteView , ProductoUpdateView , ProductoDetailView

from .router import router

app_name = "productos"

urlpatterns = [
    path("", ProductoListView.as_view(), name= "all"),
    path("create/", ProductoCreateView.as_view(), name= "create"),
    path("<int:pk>/detail/", ProductoDetailView.as_view(), name= "detail"),
    path("<int:pk>/update/", ProductoUpdateView.as_view(), name= "update"),
    path("<int:pk>/delete/", ProductoDeleteView.as_view(), name= "delete"),
]

urlpatterns += router.urls
