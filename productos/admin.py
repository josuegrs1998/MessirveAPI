from django.contrib import admin
from .models import Categoria, Subcategoria, Marca, Producto, SubcategoriaProducto, Tags, TagProducto, Imagenes, Talla, TallaProducto


admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(SubcategoriaProducto)
admin.site.register(Tags)
admin.site.register(TagProducto)
admin.site.register(Imagenes)
admin.site.register(Talla)
admin.site.register(TallaProducto)