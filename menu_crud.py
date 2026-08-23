from colors import c
from utils import limpiar_pantalla

class SubMenu():
    def __init__(self):
        pass

    def mostrar_submenu(gestor):
        opcion = 0

        while opcion != 6:
            print(f"\n{c.GRAY}[SUBMENÚ {gestor.titulo.upper()}]")
            print(f"{c.BLUE}1. Listar {gestor.titulo}")
            print(f"2. Crear {gestor.titulo}")
            print(f"3. Buscar {gestor.titulo}")
            print(f"4. Actualizar {gestor.titulo}")
            print(f"5. Eliminar {gestor.titulo}")
            print(f"6. Volver")
            print(f"0. Limpiar{c.END}\n")
            
            try:
                opcion = int(input(f"{c.GRAY}Elije una opción: {c.END}"))
                
                if opcion == 1:
                    gestor.total_lista()
                elif opcion == 2:
                    try:
                        gestor.crear()
                    except ValueError as e:
                        print(f"{c.RED}[ERROR] Método Crear: {e}{c.END}")
                elif opcion == 3:
                    try:
                        gestor.buscar()
                    except ValueError as e:
                        print(f"{c.RED}[ERROR] Método Buscar: {e}{c.END}")
                elif opcion == 4:
                    try:
                        gestor.actualizar()
                    except ValueError as e:
                        print(f"{c.RED}[ERROR] Método Actualizar: {e}{c.END}")
                elif opcion == 5:
                    try:
                        gestor.eliminar()
                    except ValueError as e:
                        print(f"{c.RED}[ERROR] Método Eliminar: {e}{c.END}")
                elif opcion == 6:
                    print(f"{c.YELLOW}Volviendo al menú principal...{c.END}\n")
                elif opcion == 0:
                    limpiar_pantalla()
                else:
                    print(f"{c.TURQUOISE}[!] Seleccione una opción válida...{c.END}")
            except ValueError:
                print(f"{c.RED}[!] ERROR: Opción ingresada no es válida !{c.END}")