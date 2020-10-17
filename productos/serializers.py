from rest_framework.serializers import ModelSerializer
from .models import Categoria,Subcategoria, Marca, Producto, Tags, TagProducto, Imagenes, Talla, TallaProducto

class CategoriaSerializer(ModelSerializer):

    class Meta:
        model = Categoria
        fields =['id','nombre', 'descripcion']


class SubcategoriaSerializer(ModelSerializer):

    class Meta:
        model = Subcategoria
        fields = '__all__'

class MarcaSerializer(ModelSerializer):

    class Meta:
        model = Marca
        fields =['id','nombre', 'descripcion']

class ProductoSerializer(ModelSerializer):
    subcategorias = SubcategoriaSerializer(many=True)
    marca = MarcaSerializer()
    class Meta:
        model = Producto
        fields = '__all__'

class SubcategoriaProductoSerializer(ModelSerializer):
    producto_set = ProductoSerializer(many=True)
    class Meta:
        model = Subcategoria
        fields ='__all__'

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