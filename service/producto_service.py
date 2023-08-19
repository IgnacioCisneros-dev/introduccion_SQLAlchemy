import db
from models.Producto import Producto
from models.producto_model import Producto as producto_model
from models.response import response
from fastapi import HTTPException


def buscar_productos():
    """Funcion que buscar los productos en la base de datos.

    Returns:
        Productos: Retorna todos los productos que estan guardados en la base de datos.
    """
    productos = db.session.query(Producto).all()
    return productos


def buscar_producto_por_sku(numero_sku):
    """Funcion que busca un producto por medio del SKU ingresado.

    Args:
        numero_sku (srt): Numero de SKU por el cual se va a buscar en base de datos.

    Returns:
        Producto: Producto obtenido de la base de datos.
    """
    producto = db.session.query(Producto).filter_by(sku=numero_sku).first()
    return producto


def persistir_producto(producto: producto_model):
    """Funcion que guarda en base de datos un nuevo producto.

    Args:
        producto (producto_model): Propiedades del producto que se va a guardar

    Returns:
        Mensaje: Mensaje indicando el estatus de la persistencia
    """

    producto_a_guardar = Producto(sku=producto.sku,
                                  bienes_transp=producto.bienes_transp,
                                  descripcion=producto.descripcion,
                                  unidad=producto.unidad,
                                  peso=producto.peso)

    db.session.add(producto_a_guardar)
    db.session.commit()
    db.session.close()

    respuesta = response(estatus='OK',
                         mensaje='Producto guardado.')
    return respuesta


def editar_producto(producto_id: int, producto: producto_model):

    respuesta = db.session.query(Producto).filter_by(id=producto_id).first()

    if not respuesta:
        raise HTTPException(status_code=404, detail='No se encontro el producto.')

    

   
    db.session.commit()
    db.session.close()
