from django.urls import path
from .views import home, agregarlibro, agregarautor, editarlibro, editarautor, eliminarlibro, eliminarautor, agregareditorial, editareditorial, elimineditorial, autores

urlpatterns = [
    path("", home, name="home"),
    path("autores", autores, name="autores"),
    path("agregar-libro/", agregarlibro, name="AppBodegas-agregar-libro"),
    path("agregar-autor/", agregarautor, name="AppBodegas-agregar-autor"),
    path("agregar-editorial/", agregareditorial, name="AppBodegas-agregar-editorial"),
    path("editar/<int:producto_id>", editarlibro, name="AppBodegas-editar"),
    path("editar-autor/<int:autor_id>", editarautor, name="AppBodegas-editar-autor"),
    path("eliminar/<int:producto_id>", eliminarlibro, name="AppBodegas-eliminar"),
    path("eliminar-autor/<int:autor_id>", eliminarautor, name="AppBodegas-eliminar-autor"),
]