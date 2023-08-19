import db
from sqlalchemy import Column, Integer, String, Float


class Producto(db.Base):

    __tablename__ = 'cat_producto_ejemplo'
    id = Column(Integer, primary_key=True)
    sku = Column(String(30), nullable=True)
    bienes_transp = Column(String(30), nullable=True)
    descripcion = Column(String(100), nullable=True)
    unidad = Column(String(6), nullable=True)
    peso = Column(Float)

    def __init__(self, sku, bienes_transp, descripcion, unidad, peso):
        self.sku = sku
        self.bienes_transp = bienes_transp
        self.descripcion = descripcion
        self.unidad = unidad
        self.peso = peso

    def __repr__(self):
        return f'cat_producto({self.sku}, {self.bienes_transp}, {self.unidad}, {self.peso})'

    def __str__(self):
        return self.sku
