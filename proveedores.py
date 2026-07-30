from time import sleep
from colors import c

class Proveedor:
    def __init__(self, nombre_proveedor):
        self.nombre_proveedor = nombre_proveedor

class GestorProveedores:
    # Variables Globales
    id_proveedor = 1

    def __init__(self):
        # Lista de proveedores
        self.lista_proveedores = []

    # -----------------------
    # CRUD de Proveedores
    # -----------------------
    
    # Crear Proveedor
    def crear_proveedor(self, proveedor: Proveedor):
        if bool(self.lista_proveedores):
            # Obtener último ID de la lista
            lista_proveedores = self.lista_proveedores[::-1]
            ultimo_id = lista_proveedores[0]["id"]
            # Aumentando el valor de ID
            ultimo_id += 1

            proveedor = {"id": ultimo_id, "nombre_proveedor": proveedor.nombre_proveedor}
            self.lista_proveedores.append(proveedor)
            print(f"{c.GREEN}[+] Proveedor creado correctamente!{c.END} - {ultimo_id}\n")
            sleep(1)
        else: 
            print(f"\n{c.GREEN}[+]{c.END} {c.GRAY}Inicializando lista proveedores{c.END}\n")
            print(f"Lista inicial: {self.lista_proveedores}")
            print(f"\n{c.GREEN}[+]{c.END} {c.TURQUOISE}Creando proveedor...{c.END}\n")
            sleep(1)
            proveedor = {"id": self.id_proveedor, "nombre_proveedor": proveedor.nombre_proveedor}
            self.lista_proveedores.append(proveedor)
            print(f"{c.GREEN}[+] Proveedor creado correctamente!{c.END} - {self.id_proveedor}\n")
            sleep(1)

    # Mostrar Total Proveedores
    def total_proveedores(self):
        print(f"Total Proveedores {len(self.lista_proveedores)}: {self.lista_proveedores}")


if __name__ == '__main__':
    # Creación del objeto Gestor Proveedors
    gestor_proveedores = GestorProveedores()
    
    proveedor_1 = Proveedor("Evercrisp") # Creación de los objetos (Proveedores)
    gestor_proveedores.crear_proveedor(proveedor_1) # Gestor de Proveedores

    proveedor_2 = Proveedor("Lays")
    gestor_proveedores.crear_proveedor(proveedor_2)

    proveedor_3 = Proveedor("Pepsico")
    gestor_proveedores.crear_proveedor(proveedor_3)
    gestor_proveedores.total_proveedores()
