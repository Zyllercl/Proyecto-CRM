from time import sleep
from colors import c
from base_crud import GestorCRUD, GestorDB

class Proveedor:
    def __init__(self, nombre_proveedor):
        self.nombre_proveedor = nombre_proveedor

class GestorProveedores(GestorCRUD, GestorDB):
    # Variables Globales
    id_proveedor = 1

    def __init__(self):
        self.lista_proveedores = [
            {"id": 1, "nombre_proveedor": "Test 1"},
            {"id": 2, "nombre_proveedor": "Test 2"},
        ]

    def _buscar_posicion(self, id):
        # * Obtener el indice de lista proveedores
        for i in range(len(self.lista_proveedores)):
            if self.lista_proveedores[i]["id"] == id:
                return i
        return -1

    # -----------------------
    # * CRUD de Proveedores
    # -----------------------
    def crear(self, proveedor: Proveedor):
        if bool(self.lista_proveedores):
            lista_invertida = self.lista_proveedores[::-1]
            ultimo_id = lista_invertida[0]["id"]
            ultimo_id += 1 # * Aumentando el valor de ID

            proveedor = {"id": ultimo_id, "nombre_proveedor": proveedor.nombre_proveedor}
            self.lista_proveedores.append(proveedor)
            print(f"{c.GREEN}[+] Proveedor creado{c.END} - {ultimo_id}\n")
            sleep(0.5)
        else: 
            print(f"\n{c.GREEN}[+]{c.END} {c.GRAY}Inicializando lista proveedores{c.END}\n")
            proveedor = {"id": self.id_proveedor, "nombre_proveedor": proveedor.nombre_proveedor}
            self.lista_proveedores.append(proveedor)
            print(f"{c.GREEN}[+] Proveedor creado{c.END} - {self.id_proveedor}\n")
            sleep(0.5)

    def actualizar(self, id_proveedor, nuevo_nombre):
        posicion = self._buscar_posicion(id_proveedor)

        if posicion != -1:
            self.lista_proveedores[posicion]["nombre_proveedor"] = nuevo_nombre
            print(f"{c.GREEN}[+] Proveedor actualizado{c.END}\n")
        else:
            print(f"{c.RED}[!] ERROR: Proveedor no encontrado.{c.END}\n")

    def eliminar(self, id_proveedor):
        posicion = self._buscar_posicion(id_proveedor)

        if id_proveedor == 0:
            print(f"{c.RED}[!] Error: El ID no puede ser 0 !{c.END}")
            return
        
        if posicion != -1:
            del self.lista_proveedores[posicion]
            print(f"{c.GRAY}[-] Proveedor eliminado.{c.END}\n")
        else:
            print(f"{c.RED}[!] ERROR: Proveedor no encontrado.{c.END}")

    def leer(self):
        pass

    def buscar_por_id(self, id_proveedor):
        posicion = self._buscar_posicion(id_proveedor)

        if posicion != -1:
            print(f"{c.GREEN}Proveedor encontrado: {self.lista_proveedores[posicion]["nombre_proveedor"]}{c.END}\n")
        else:
            print(f"{c.RED}[!] ERROR: Proveedor no existe.{c.END}\n")

    def total_lista(self):
        if (bool(self.lista_proveedores)):
            print(f"Total Proveedores {len(self.lista_proveedores)}: {self.lista_proveedores}")
        else:
            print(f"{c.RED}[!] No hay proveedores.{c.END}")