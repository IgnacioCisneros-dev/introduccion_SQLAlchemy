import db
from models.Producto import Producto


def run():
    primer_registro = Producto('16653',
                               'bienes',
                               'test',
                               'pieza',
                               2.2)
    # Se agrega a la sesion
    db.session.add(primer_registro)

    # Se hace el commit para guardar en la base
    db.session.commit()
    print(f'Id del primer registro insetado en la base: {primer_registro.id}')
    print('Consultando en base de datos.')

    # Para obtener todos los registros de la tabla de productos.
    consulta = db.session.query(Producto).all()

    for item in consulta:
        print(f'Registros de base de datos: {item}')

    # Para contar cuantos registros hay en la tabla
    total_de_productos = db.session.query(Producto).count()
    print(
        f'El total de registros en la tabla productos es: {total_de_productos}')

    # Filtrando, es lo mismo que el WHERE
    test = db.session.query(Producto).filter_by(descripcion='prueba').first()
    filtrado = db.session.query(Producto).filter(Producto.sku == 16653).all()

    print(f'Primer filtrado: {test}')
    print(f'Segundo filtrado: {filtrado}')

    pass


if __name__ == '__main__':
    db.Base.metadata.create_all(db.motor)
    run()
