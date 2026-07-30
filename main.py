from colors import c

# Menú Interactivo
def menu():
    print(f"{c.GRAY}Menú CRM{c.END}")
    print(f"{c.BLUE}1. Ventas")
    print(f"2. Inventario")
    print(f"3. Proveedores")
    print(f"4. Salir{c.END}\n")

# Función principal de la APP
def app():
    print(f"\n{c.YELLOW}Inicialización Aplicación CRM{c.END}\n")

    menu()

    opcion = 0

    while opcion != 4:
        # Opción ingresada por usuario
        opcion = int(input("Elije una opcion: "))       
        
        if opcion == 1:
            print(f"\n{c.GREEN}[!] Proximamente...{c.END}\n")
        elif opcion == 2:
            print(f"\n{c.GREEN}[!] Proximamente...{c.END}\n")
        elif opcion == 3:
            print(f"\n{c.GREEN}[!] Proximamente...{c.END}\n")
        elif opcion == 4:
            print(f"\n{c.RED}Finalizando programa...{c.END}")
        else:
            print(f"\n{c.TURQUOISE}[!] Seleccione una opción válida...{c.END}\n")

if __name__ == "__main__":
    app()