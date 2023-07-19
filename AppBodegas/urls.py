from django.urls import path
from .views import home, agregarlibro, agregarautor, editarlibro, editarautor, eliminarlibro, eliminarautor, agregareditorial, editareditorial, eliminareditorial, autores, editoriales

urlpatterns = [
    path("", home, name="home"),
    path("autores", autores, name="autores"),
    path("editoriales", editoriales, name="editoriales"),
    path("agregar-libro/", agregarlibro, name="AppBodegas-agregar-libro"),
    path("agregar-autor/", agregarautor, name="AppBodegas-agregar-autor"),
    path("agregar-editorial/", agregareditorial, name="AppBodegas-agregar-editorial"),
    path("editar/<int:producto_id>", editarlibro, name="AppBodegas-editar"),
    path("editar-autor/<int:autor_id>", editarautor, name="AppBodegas-editar-autor"),
    path("editar-editorial/<int:editorial_id>", editareditorial, name="AppBodegas-editar-editorial"),
    path("eliminar/<int:producto_id>", eliminarlibro, name="AppBodegas-eliminar"),
    path("eliminar-autor/<int:autor_id>", eliminarautor, name="AppBodegas-eliminar-autor"),
    path("eliminar-editorial/<int:editorial_id>", eliminareditorial, name="AppBodegas-eliminar-editorial"),
]