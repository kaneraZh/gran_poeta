from django.urls import path
from .views import home, agregar, editar, eliminar

urlpatterns = [
    path("", home, name="home"),
    path("agregar/", agregar, name="AppNota-agregar"),
    path("editar/<int:nota_id>", editar, name="AppNota-editar"),
    path("eliminar/<int:nota_id>", eliminar, name="AppNota-eliminar"),
]