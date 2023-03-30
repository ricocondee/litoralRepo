#Andrus Correa Web A
def mejor_opcion_libro(libros):
    mejor_libro = None
    mejor_ganancia = 0

    for libro in libros:
        cantidad = libro['cantidad']
        precio = libro['precio']
        costo = libro['costo']

        if cantidad >= 100:
            if cantidad > 800:
                precio = precio * 1.1

            ganancia = (precio - costo)

            if ganancia > 14000 and ganancia > mejor_ganancia:
                mejor_ganancia = ganancia
                mejor_libro = libro

    if mejor_libro is not None:
        return f"El mejor libro para vender es {mejor_libro['nombre']}, de {mejor_libro['autor']}, con código {mejor_libro['codigo']}, publicado en {mejor_libro['año_publicacion']} y precio de venta de ${mejor_libro['precio']}."
    else:
        return "Ninguno de los libros es la mejor opción para ser vendido."

libros = [
    {
        'nombre': 'Harry Potter y la piedra filosofal',
        'codigo': 'HPJK1997',
        'autor': 'J.K Rowling',
        'año_publicacion': 1997,
        'cantidad': 200,
        'precio': 25000,
        'costo': 9000
    },
    {
        'nombre': 'Los Juegos del Hambre',
        'codigo': 'JHSC2008',
        'autor': 'Suzanne Collins',
        'año_publicacion': 2008,
        'cantidad': 20,
        'precio': 27000,
        'costo': 12000
    },
    {
        'nombre': 'El Hobbit',
        'codigo': 'EHJR1937',
        'autor': 'J.R.R. Tolkien',
        'año_publicacion': 1937,
        'cantidad': 100,
        'precio': 35000,
        'costo': 15000
    },
    {
        'nombre': 'Hamlet',
        'codigo': 'HWS1589',
        'autor': 'William Shakespeare',
        'año_publicacion': 1589,
        'cantidad': 20,
        'precio': 26000,
        'costo': 13000
    }
]

print(mejor_opcion_libro(libros))
