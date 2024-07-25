from flask_marshmallow import Marshmallow

ma = Marshmallow()

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('ProductoID', 'Nombre', 'Descripcion', 'Precio', 'CantidadEnInventario', 'CategoriaID', 'ProveedorID')

# Instancias del esquema
product_schema = ProductSchema()  # para un solo producto
products_schema = ProductSchema(many=True)  # para múltiples productos
