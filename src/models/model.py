from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Producto(db.Model):
    __tablename__ = 'Productos'
    ProductoID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Descripcion = db.Column(db.Text)
    Precio = db.Column(db.Numeric(10, 2), nullable=False)
    CantidadEnInventario = db.Column(db.Integer, nullable=False)
    CategoriaID = db.Column(db.Integer, nullable=True)
    ProveedorID = db.Column(db.Integer, nullable=True)

    def __init__(self, nombre, descripcion, precio, cantidad_en_inventario, categoria_id, proveedor_id):
        self.Nombre = nombre
        self.Descripcion = descripcion
        self.Precio = precio
        self.CantidadEnInventario = cantidad_en_inventario
        self.CategoriaID = categoria_id
        self.ProveedorID = proveedor_id