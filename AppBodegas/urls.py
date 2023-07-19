from django.urls import path
from .views import home, agregarlibro, agregarautor, editarlibro, editarautor, eliminarlibro, eliminarautor 

urlpatterns = [
    path("", home, name="home"),
    path("agregar-libro/", agregarlibro, name="AppBodegas-agregar-libro"),
    path("agregar-autor/", agregarautor, name="AppBodegas-agregar-autor"),
    path("editar/<int:producto_id>", editarlibro, name="AppBodegas-editar"),
    path("eliminar/<int:producto_id>", eliminarlibro, name="AppBodegas-eliminar"),
]