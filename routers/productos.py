from fastapi import APIRouter
from service.producto_service import buscar_productos, buscar_producto_por_sku, persistir_producto, editar_producto
from models.Producto import Producto
from models.response import response
from models.producto_model import Producto as producto_model

router_productos = APIRouter(prefix='/productos',
                             tags=["Productos."])


@router_productos.get("/obtener",
                      summary='Lista de productos.',
                      description='Recupera una lista de productos de la base de datos.')
def obtener_productos():
    """Funcion que invoca a la funcion de buscar_productos()

    Returns:
        Productos: Productos obtenidos de la base de datos.
    """
    resultado = buscar_productos()
    return resultado


@router_productos.get("/obtener/{numero_sku}",
                      summary='Productos.',
                      description='Muestra un producto obtenido por el numero de SKU.')
def obtener_producto_por_sku(numero_sku: str):
    """Funcion del servicio que busca un producto por el SKU ingresado.

    Args:
        numero_sku (str): numero de SKU por el cual se va a buscar el producto en la base de datos.

    Returns:
        Producto: Producto en caso de exister en la base de datos, en caso contrario regresa un mensaje.
    """
    resultado = buscar_producto_por_sku(numero_sku)
    if resultado is None:
        return f'No se encontro producto con el SKU {numero_sku}'
    else:
        return resultado


@router_productos.post("/guardar",
                       summary='Guarda un producto.',
                       description='Persiste un producto en el sistema.', response_model=response)
def guardar_producto(producto: producto_model):
    """Funcion que invoca al servicio para persistir un producto en el sistema.

    Args:
        producto (producto_model): Request del producto que se va a guardar.

    Returns:
        Mensaje: Mensaje de respuesta del guardado.
    """
    respuesta = persistir_producto(producto)
    return respuesta

@router_productos.put("/actualizar",
                       summary='Actualiza un producto.',
                       description='Actualiza un producto en el sistema.', response_model=response)
def actualizar_producto():
    editar_producto()

