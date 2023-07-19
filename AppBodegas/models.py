from django.db import models

class Nota(models.Model):
    nota = models.CharField(max_length=100)
    def __str__(self):
        return self.nota

class Autor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    def __str__(self) -> str:
        return self.nombre

class Editorial(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    def __str__(self) -> str:
        return self.nombre

class ProductoTipo(models.Model):
    id = models.BigAutoField(primary_key='id')
    nombre = models.CharField(max_length=45)
    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    id = models.BigAutoField(primary_key='id')
    producto_tipo_id = models.ForeignKey(ProductoTipo, to_field='id', on_delete=models.PROTECT)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    def __str__(self) -> str:
        return f'{self.nombre}, {self.descripcion}, {self.producto_tipo_id}'

class ProductoAutor(models.Model):
    producto_id = models.ForeignKey(Producto, to_field='id', on_delete=models.PROTECT)
    autor_id = models.ForeignKey(Autor, to_field='id', on_delete=models.PROTECT)
    def __str__(self) -> str:
        return f'{self.autor_id}'

class ProductoEditorial(models.Model):
    producto_id = models.ForeignKey(Producto, to_field='id', on_delete=models.PROTECT)
    editorial_id = models.ForeignKey(Editorial, to_field='id', on_delete=models.PROTECT)
    def __str__(self) -> str:
        return f'{self.editorial_id}'

class Usuario(models.Model):
    id = models.BigAutoField(primary_key='id')
    nombre = models.CharField(max_length=16)
    email = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=32)
    fecha_creacion = models.DateTimeField()
    def __str__(self) -> str:
        return f'{self.nombre}'

class Bodega(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.nombre}'

class BodegaInventario(models.Model):
    bodega_id = models.ForeignKey(Bodega, to_field='id', on_delete=models.PROTECT)
    producto_id = models.ForeignKey(Producto, to_field='id', on_delete=models.PROTECT)
    cantidad = models.IntegerField(blank=False)
    def __str__(self) -> str:
        return f'{self.producto_id}x{self.cantidad}'

class Informe(models.Model):
    id = models.BigAutoField(primary_key=True)
    autor_id = models.ForeignKey(Usuario, to_field='id', on_delete=models.PROTECT)
    origen_id = models.ForeignKey(Bodega, to_field='id', on_delete=models.PROTECT, related_name='origen_id')
    destino_id = models.ForeignKey(Bodega, to_field='id', on_delete=models.PROTECT, related_name='destino_id')
    fecha = models.DateField(blank=False)
    def __str__(self) -> str:
        return f'{self.fecha} : {self.origen_id}->{self.destino_id}, {self.autor_id}'

class InformeInventario(models.Model):
    informe_id = models.ForeignKey(Informe, to_field='id', on_delete=models.PROTECT)
    producto_id = models.ForeignKey(Producto, to_field='id', on_delete=models.PROTECT)
    cantidad = models.IntegerField(blank=False)
    def __str__(self) -> str:
        return f'{self.informe_id}, {self.producto_id}x{self.cantidad}'
