from colors import c
from proveedores import GestorProveedores

class SubMenu():
    def __init__(self):
        self.crud_proveedor = GestorProveedores()
        self.mostrar_submenu()

    def mostrar_submenu(self):
        opcion = 0

        while opcion != 5:
            print(f"\n{c.BLUE}1. Listar proveedores")
            print(f"2. Crear proveedor")
            print(f"3. Buscar proveedor")
            print(f"4. Eliminar proveedor")
            print(f"5. Volver{c.END}\n")
            
            try:
                opcion = int(input(f"{c.GRAY}Elije una opcion (submenu): {c.END}"))
                
                if opcion == 1:
                    self.crud_proveedor.total_proveedores()
                elif opcion == 2:
                    print(f"\n{c.GREEN}[!] Proximamente...{c.END}\n")
                elif opcion == 3:
                    print(f"\n{c.GREEN}[!] Proximamente...{c.END}\n")
                elif opcion == 4:
                    print(f"\n{c.GREEN}[!] Proximamente...{c.END}\n")
                elif opcion == 5:
                    print(f"\n{c.YELLOW}Volviendo al menú principal...{c.END}\n")
                else:
                    print(f"\n{c.TURQUOISE}[!] Seleccione una opción válida...{c.END}\n")
            except ValueError:
                print(f"{c.RED}[!] ERROR: Opción ingresada no es válida !{c.END}")