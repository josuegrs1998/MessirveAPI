from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre


class Subcategoria(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    codigoProducto = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=120)
    activo = models.BooleanField()
    tipoMaterial = models.CharField(max_length=30)
    exento = models.BooleanField()
    idMarca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class SubcategoriaProducto(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idSubcategoria = models.ForeignKey(Subcategoria , on_delete=models.CASCADE)

class Tags(models.Model):
    nombre = models.CharField(max_length=60)
    def __str__(self):
        return self.nombre
    
class TagProducto(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idTag = models.ForeignKey(Tags, on_delete=models.CASCADE)

class Imagenes(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField()

class Talla(models.Model):
    tamanio = models.CharField(max_length=15)
    def __str__(self):
        return self.tamanio

class TallaProducto(models.Model):
    idtalla = models.ForeignKey(Talla, on_delete=models.CASCADE )
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()








