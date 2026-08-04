from colors import c
from menu_crud import SubMenu

def menu():
    print(f"{c.GRAY}Menú CRM{c.END}")
    print(f"{c.BLUE}1. Ventas")
    print(f"2. Inventario")
    print(f"3. Proveedores")
    print(f"4. Salir{c.END}\n")
    
def app():
    print(f"\n{c.YELLOW}Inicialización Aplicación CRM{c.END}\n")
    opcion = 0

    while opcion != 4:
        menu()
        try:
            opcion = int(input(f"{c.GRAY}Elije una opcion: {c.END}"))
            
            if opcion == 1:
                print(f"\n{c.GREEN}[!] Proximamente...{c.END}\n")
            elif opcion == 2:
                print(f"\n{c.GREEN}[!] Proximamente...{c.END}\n")
            elif opcion == 3:
                SubMenu()
                opcion = 0 # * Se vuelve a mostrar el menú principal
            elif opcion == 4:
                print(f"\n{c.RED}Finalizando programa...{c.END}")
            else:
                print(f"\n{c.TURQUOISE}[!] Seleccione una opción válida...{c.END}\n")
        except ValueError:
            print(f"{c.RED}[!] ERROR: Opción ingresada no es válida !{c.END}")

if __name__ == "__main__":
    app()