from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Autor, Producto, Editorial
from .forms import crear_producto, crear_autor, crear_editorial
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

def autores(request):
    autores=Autor.objects.all()
    context={
        "autores":autores
    }
    return render(request, "AppBodegas/autores.html", context)


def agregarautor(request):
    if request.method == "POST":
        form = crear_autor(request.POST)
        if form.is_valid:
            form.save()
            return redirect("autores")
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
            return redirect("autores")
    else:
        form = crear_autor(instance=autor)    
    context={"form":form}
    return render(request, "AppBodegas/agregar-autor.html", context)

def eliminarautor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect("autores")



    #------------------------------------------------------------------#

def agregareditorial(request):
    if request.method == "POST":
        form = crear_editorial(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = crear_editorial()
    context = {
        "form":form
    }
    return render(request, "AppBodegas/agregar-editorial.html", context)
    
def editareditorial(request, editorial_id):
    editorial = Editorial.objects.get(id=editorial_id)
    if request.method == "POST":
        form = crear_editorial(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = crear_editorial(instance=editorial)    
    context={"form":form}
    return render(request, "AppBodegas/agregar-editorial.html", context)

def elimineditorial(request, editorial_id):
    editorial = Editorial.objects.get(id=editorial_id)
    editorial.delete()
    return redirect("home")

