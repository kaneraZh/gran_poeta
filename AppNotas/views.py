from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Nota
from .forms import NotaForm
from django.shortcuts import redirect

# Create your views here.

def home(request):
    notas=Nota.objects.all()
    context={
        "notas":notas
    }
    return render(request, "AppNotas/home.html", context)

def agregar(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = NotaForm()
    context = {
        "form":form
    }
    return render(request, "AppNotas/agregar.html", context)
    
def editar(request, nota_id):
    nota = Nota.objects.get(id=nota_id)
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NotaForm(instance=nota)    
    context={"form":form}
    return render(request, "AppNotas/agregar.html", context)

def eliminar(request, nota_id):
    nota = Nota.objects.get(id=nota_id)
    nota.delete()
    return redirect("home")

