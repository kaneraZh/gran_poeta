from django import forms
from .models import Nota, Producto

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ["nota"]

class crear_producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["producto_tipo_id",
                  "nombre",
                  "descripcion"]
