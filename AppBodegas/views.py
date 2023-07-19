from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Nota, Producto
from .forms import crear_producto, crear_producto
from django.shortcuts import redirect

# Create your views here.

def home(request):
    productos=Producto.objects.all()
    context={
        "productos":productos
    }
    return render(request, "AppBodegas/home.html", context)

def agregar(request):
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
    return render(request, "AppBodegas/agregar.html", context)
    
def editar(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == "POST":
        form = crear_producto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = crear_producto(instance=producto)    
    context={"form":form}
    return render(request, "AppBodegas/agregar.html", context)

def eliminar(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect("home")

