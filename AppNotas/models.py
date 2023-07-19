from django.db import models

class Nota(models.Model):
    nota = models.CharField(max_length=100)
    def __str__(self):
        return self.nota

class Autor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

class Editorial(models.Model):
    id = models.BigAutoField(primary_key=True)

class ProductoTipo(models.Model):
    id = models.BigAutoField(primary_key='id')
    nombre = models.CharField(max_length=45)

class Producto(models.Model):
    id = models.BigAutoField(primary_key='id')
    producto_tipo_id = models.ForeignKey(ProductoTipo, to_field='id', on_delete=models.PROTECT)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

class ProductoAutor(models.Model):
    producto_id = models.ForeignKey(Producto, to_field='id', on_delete=models.PROTECT)
    autor_id = models.ForeignKey(Autor, to_field='id', on_delete=models.PROTECT)

class ProductoEditorial(models.Model):
    producto_id = models.ForeignKey(Producto, to_field='id', on_delete=models.PROTECT)
    editorial_id = models.ForeignKey(Editorial, to_field='id', on_delete=models.PROTECT)

class Usuario(models.Model):
    id = models.BigAutoField(primary_key='id')
    nombre = models.CharField(max_length=16)
    email = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=32)
    fecha_creacion = models.DateTimeField()

class Bodega(models.Model):
    id = models.BigAutoField(primary_key=True)

class BodegaInventario(models.Model):
    bodega_id = models.ForeignKey(Bodega, to_field='id', on_delete=models.PROTECT)
    producto_id = models.ForeignKey(Producto, to_field='id', on_delete=models.PROTECT)
    cantidad = models.IntegerField(blank=False)

class Informe(models.Model):
    id = models.BigAutoField(primary_key=True)
    autor_id = models.ForeignKey(Usuario, to_field='id', on_delete=models.PROTECT)
    origen_id = models.ForeignKey(Bodega, to_field='id', on_delete=models.PROTECT, related_name='origen_id')
    destino_id = models.ForeignKey(Bodega, to_field='id', on_delete=models.PROTECT, related_name='destino_id')
    fecha = models.DateField(blank=False)

class InformeInventario(models.Model):
    informe_id = models.ForeignKey(Informe, to_field='id', on_delete=models.PROTECT)
    producto_id = models.ForeignKey(Producto, to_field='id', on_delete=models.PROTECT)
    cantidad = models.IntegerField(blank=False)
