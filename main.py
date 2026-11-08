from utilidades import (registrar_libro, buscar_libro, catalogo_ordenado,
                        registrar_socio, existe_socio, registrar_prestamo,
                        analizar_prestamos)

catalogo = {
    "L003": {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
    "L001": {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
    "L005": {"titulo": "Cosmos", "autor": "Carl Sagan"},
    "L002": {"titulo": "Breve historia del tiempo", "autor": "Stephen Hawking"},
    "L004": {"titulo": "El origen de las especies", "autor": "Charles Darwin"},
}
socios = {"S001", "S002", "S003", "S004", "S005"}
prestamos_novela = {"S001", "S002", "S003"}
prestamos_ciencia = {"S003", "S004"}

def main():
    try:
        while True:
            print("\nBiblioteca")
            print("1. Registrar libro")
            print("2. Buscar libro por código")
            print("3. Ver catálogo ordenado")
            print("4. Registrar socio")
            print("5. Verificar socio")
            print("6. Registrar préstamo")
            print("7. Análisis de préstamos")
            print("0. Salir")
            opcion = input("Opción: ").strip()
            if opcion == "1":
                codigo = input("Código: ").strip().upper()
                titulo = input("Título: ").strip()
                autor = input("Autor: ").strip()
                if not codigo or not titulo or not autor:
                    print("Todos los campos son obligatorios")
                elif registrar_libro(catalogo, codigo, titulo, autor):
                    print("Libro registrado")
                else:
                    print("Ya existe un libro con ese código")
            elif opcion == "2":
                libro = buscar_libro(catalogo, input("Código: ").strip().upper())
                if libro:
                    print(f"{libro['titulo']} - {libro['autor']}")
                else:
                    print("No existe un libro con ese código")
            elif opcion == "3":
                for codigo, libro in catalogo_ordenado(catalogo).items():
                    print(codigo, libro["titulo"], libro["autor"])
            elif opcion == "4":
                id_socio = input("ID del socio: ").strip().upper()
                if not id_socio:
                    print("El ID no puede estar vacío")
                elif registrar_socio(socios, id_socio):
                    print("Socio registrado")
                else:
                    print("El socio ya está registrado")
            elif opcion == "5":
                if existe_socio(socios, input("ID del socio: ").strip().upper()):
                    print("El socio está registrado")
                else:
                    print("El socio no está registrado")
            elif opcion == "6":
                id_socio = input("ID del socio: ").strip().upper()
                genero = input("Género (1 novela, 2 ciencia): ").strip()
                if genero not in ("1", "2"):
                    print("Género no válido")
                else:
                    prestamos = prestamos_novela if genero == "1" else prestamos_ciencia
                    if registrar_prestamo(socios, prestamos, id_socio):
                        print("Préstamo registrado")
                    else:
                        print("El socio no está registrado")
            elif opcion == "7":
                ambos, solo_novela, total = analizar_prestamos(prestamos_novela, prestamos_ciencia)
                print("Leen novela y ciencia:", sorted(ambos))
                print("Solo leen novela:", sorted(solo_novela))
                print("Total de socios con préstamos:", len(total), sorted(total))
            elif opcion == "0":
                print("Hasta luego")
                break
            else:
                print("Opción no válida")
    except (EOFError, KeyboardInterrupt):
        print("\nHasta luego")

if __name__ == "__main__":
    main()
