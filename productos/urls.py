from django.urls import path
from .views import (ListaCategoria, DetalleCategoria, ListaSubcategoria, ListaImagenes,
DetalleImagenes, ListaTalla, DetalleTalla, ListaTallaProducto, DetalleTallaProducto,
DetalleSubcategoria,ListaMarca, DetalleMarca, ListaProducto, ListaTag, DetalleTag,
ListaTagProductos, DetalleTagProductos, DetalleProducto)


urlpatterns =[
    path('categorias', ListaCategoria.as_view()),
    path('categorias/<int:id>', DetalleCategoria.as_view()),
    path('subcategorias', ListaSubcategoria.as_view()),
    path('subcategorias/<int:id>', DetalleSubcategoria.as_view()),
    path('marcas', ListaMarca.as_view()),
    path('marcas/<int:id>', DetalleMarca.as_view()),
    path('productos', ListaProducto.as_view()),
    path('productos/<int:id>', DetalleProducto.as_view()),
    #path('subproductos', ListaSubProducto.as_view()),
    #path('subproductos/<int:id>', DetalleSubProducto.as_view()),
    path('tags', ListaTag.as_view()),
    path('tags/<int:id>', DetalleTag.as_view()),
    path('tagproductos', ListaTagProductos.as_view()),
    path('tagproductos/<int:id>', DetalleTagProductos.as_view()),
    path('imagenes', ListaImagenes.as_view()),
    path('imagenes/<int:id>', DetalleImagenes.as_view()),
    path('talla', ListaTalla.as_view()),
    path('talla/<int:id>', DetalleTalla.as_view()),
    path('tallaproducto', ListaTallaProducto.as_view()),
    path('tallaproducto/<int:id>', DetalleTallaProducto.as_view())

]