from rest_framework.serializers import ModelSerializer
from .models import Categoria,Subcategoria, Marca, Producto, Tags, TagProducto, Imagenes, Talla, TallaProducto

class CategoriaSerializer(ModelSerializer):

    class Meta:
        model = Categoria
        fields =['id','nombre', 'descripcion']


class SubcategoriaSerializer(ModelSerializer):

    class Meta:
        model = Subcategoria
        fields = ['id', 'nombre', 'descripcion', 'idCategoria']

class MarcaSerializer(ModelSerializer):

    class Meta:
        model = Marca
        fields =['id','nombre', 'descripcion']

class ProductoSerializer(ModelSerializer):
    subCategorias = SubcategoriaSerializer(many=True)
    class Meta:
        model = Producto
        fields ='__all__'

#class SubcategoriaProductoSerializer(ModelSerializer):

    #class Meta:
     #   model = SubcategoriaProducto
      #  fields =['id', 'idProducto', 'idSubcategoria']

class TagSerializer(ModelSerializer):
    
    class Meta:
        model = Tags
        fields =['id', 'nombre']

class TagProductoSerializer(ModelSerializer):

    class Meta:
        model = TagProducto
        fields =['id', 'idTag', 'idProducto']

class ImagenesSerializer(ModelSerializer):

    class Meta: 
        model = Imagenes
        fields = ['id', 'idProducto', 'imagen']

class TallaSerializer(ModelSerializer):

    class Meta:
        model = Talla
        fields = ['id', 'tamanio']

class TallaProductoSerializer(ModelSerializer):

    class Meta:
        model = TallaProducto
        fields = ['id', 'idtalla', 'idProducto', 'cantidad']