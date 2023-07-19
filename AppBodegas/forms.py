from django import forms

from .models import Producto, ProductoAutor, ProductoEditorial
class crear_producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["producto_tipo_id",
                  "nombre",
                  "descripcion"]
#    
#    class Meta:
#        model = ProductoEditorial
#        fields = ["editorial_id"]
#    
#    class Meta:
#        model = ProductoAutor
#        fields = ["autor_id"]

from .models import Autor
class crear_autor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre"]

from .models import Editorial
class crear_editorial(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ["nombre"]
