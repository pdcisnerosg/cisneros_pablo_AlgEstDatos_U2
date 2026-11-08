# Biblioteca

Programa de consola en Python que gestiona el catálogo y los préstamos de una biblioteca con las estructuras de la Unidad 2: diccionarios y conjuntos.

Autor: Pablo Cisneros. Materia: Algoritmos y Estructuras de Datos (Ciencia de Datos).

## Cómo ejecutar

Requiere Python 3 y no usa librerías externas.

```
python main.py
```

En Mac o Linux, si `python` no funciona, usa `python3 main.py`. El programa ya incluye 5 libros y 5 socios de ejemplo, así que se puede probar de inmediato.

## Archivos

| Archivo | Contenido |
|---|---|
| `main.py` | Datos de ejemplo y menú de consola |
| `utilidades.py` | Funciones de los cuatro requerimientos |

## Requerimientos

**R1 – Catálogo de libros (diccionario).** La clave es el código del libro y el valor es otro diccionario con título y autor. Permite registrar un libro (opción 1) y buscarlo por su código de forma inmediata (opción 2).

**R2 – Catálogo ordenado (TreeMap).** Muestra el catálogo ordenado por código con `sorted()` (opción 3).

**R3 – Socios registrados (conjunto).** Guarda los identificadores de los socios en un `set`. Evita duplicados al registrar (opción 4) y verifica al instante si un ID existe (opción 5).

**R4 – Análisis de préstamos (operaciones entre conjuntos).** Cada préstamo agrega al socio al conjunto de novela o de ciencia (opción 6), siempre que esté registrado. El análisis (opción 7) muestra los socios que leen ambos géneros (intersección), los que solo leen novela (diferencia) y el total de socios distintos con préstamos (unión).

## Complejidades

| Función | Complejidad | Justificación |
|---|---|---|
| `registrar_libro` | O(1) | Insertar en un diccionario calcula el hash de la clave. |
| `buscar_libro` | O(1) | El hash de la clave lleva directo al libro. |
| `catalogo_ordenado` | O(n log n) | `sorted()` ordena las n claves. |
| `registrar_socio` | O(1) | Verificar y agregar en un conjunto usa el hash. |
| `existe_socio` | O(1) | La pertenencia en un conjunto usa el hash. |
| `registrar_prestamo` | O(1) | Una verificación y una inserción en conjuntos. |
| `analizar_prestamos` | O(n) | Intersección, diferencia y unión recorren los elementos una vez. |

Las complejidades de diccionarios y conjuntos son del caso promedio; en el peor caso, con todas las claves en colisión, serían O(n).
