from django.urls import path
from .views import home, agregar, editar, eliminar

urlpatterns = [
    path("", home, name="home"),
    path("agregar/", agregar, name="AppBodega-agregar"),
    path("editar/<int:producto_id>", editar, name="AppBodega-editar"),
    path("eliminar/<int:producto_id>", eliminar, name="AppBodega-eliminar"),
]