# R1 - Catálogo de libros (dict)
# registrar_libro: O(1)
def registrar_libro(catalogo, codigo, titulo, autor):
    if codigo in catalogo:
        return False
    catalogo[codigo] = {"titulo": titulo, "autor": autor}
    return True

# buscar_libro: O(1)
def buscar_libro(catalogo, codigo):
    return catalogo.get(codigo)

# R2 - Catálogo ordenado (TreeMap)
# catalogo_ordenado: O(n log n), un SortedDict ya lo tendría ordenado
def catalogo_ordenado(catalogo):
    return {codigo: catalogo[codigo] for codigo in sorted(catalogo)}

# R3 - Socios registrados (set)
# registrar_socio: O(1)
def registrar_socio(socios, id_socio):
    if id_socio in socios:
        return False
    socios.add(id_socio)
    return True

# existe_socio: O(1)
def existe_socio(socios, id_socio):
    return id_socio in socios

# R4 - Análisis de préstamos (operaciones entre conjuntos)
# registrar_prestamo: O(1)
def registrar_prestamo(socios, prestamos, id_socio):
    if id_socio not in socios:
        return False
    prestamos.add(id_socio)
    return True

# analizar_prestamos: O(n)
def analizar_prestamos(novela, ciencia):
    ambos = novela & ciencia
    solo_novela = novela - ciencia
    total = novela | ciencia
    return ambos, solo_novela, total
