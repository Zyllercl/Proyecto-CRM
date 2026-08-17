from colors import c

class SubMenu():
    def __init__(self):
        pass

    def mostrar_submenu(gestor):
        opcion = 0

        while opcion != 6:
            print(f"\n{c.BLUE}1. Listar proveedores")
            print(f"2. Crear proveedor")
            print(f"3. Buscar proveedor")
            print(f"4. Actualizar proveedor")
            print(f"5. Eliminar proveedor")
            print(f"6. Volver{c.END}\n")
            
            try:
                opcion = int(input(f"{c.GRAY}Elije una opcion (submenu): {c.END}"))
                
                if opcion == 1:
                    gestor.total_lista()
                elif opcion == 2:
                    try:
                        gestor.crear()
                    except ValueError as e:
                        print(f"{c.RED}[ERROR] SubMenu: {e}{c.END}")
                elif opcion == 3:
                    print(f"{c.GREEN}[!] Proximamente...{c.END}")
                elif opcion == 4:
                    try:
                        gestor.actualizar()
                    except ValueError as e:
                        print(f"{c.RED}[ERROR] SubMenu: {e}{c.END}")
                elif opcion == 5:
                    print(f"{c.GREEN}[!] Proximamente...{c.END}")
                elif opcion == 6:
                    print(f"{c.YELLOW}Volviendo al menú principal...{c.END}\n")
                else:
                    print(f"{c.TURQUOISE}[!] Seleccione una opción válida...{c.END}")
            except ValueError:
                print(f"{c.RED}[!] ERROR: Opción ingresada no es válida !{c.END}")