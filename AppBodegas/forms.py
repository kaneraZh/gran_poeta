from django import forms
from .models import Autor, Producto



class crear_producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["producto_tipo_id",
                  "nombre",
                  "descripcion"]

class crear_autor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre"]


                  