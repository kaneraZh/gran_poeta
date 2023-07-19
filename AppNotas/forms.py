from django import forms
from .models import Nota, Producto

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ["nota"]

class CrearNuevoLibro(forms.Form):
    title = forms.CharField(label="Titulo del libro", max_length=200)
    description = forms.CharField(label="Descriccion del libro", widget=forms.Textarea)
