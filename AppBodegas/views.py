from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Producto, Bodega, Autor
from .forms import crear_producto, crear_autor
from django.shortcuts import redirect

# Create your views here.

def home(request):
    productos=Producto.objects.all()
    #productos=Producto.objects.select_related('ProductoAutor', 'ProductoEditorial')
    context={
        "productos":productos
    }
    return render(request, "AppBodegas/home.html", context)

def agregarlibro(request):
    if request.method == "POST":
        form = crear_producto(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = crear_producto()
    context = {
        "form":form
    }
    return render(request, "AppBodegas/agregar-libro.html", context)
    
def editarlibro(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == "POST":
        form = crear_producto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = crear_producto(instance=producto)    
    context={"form":form}
    return render(request, "AppBodegas/agregar-libro.html", context)

def eliminarlibro(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect("home")

#------------------------------------------------------------------#


def agregarautor(request):
    if request.method == "POST":
        form = crear_autor(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = crear_autor()
    context = {
        "form":form
    }
    return render(request, "AppBodegas/agregar-autor.html", context)
    
def editarautor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    if request.method == "POST":
        form = crear_autor(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = crear_autor(instance=autor)    
    context={"form":form}
    return render(request, "AppBodegas/agregar-autor.html", context)

def eliminarautor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect("home")