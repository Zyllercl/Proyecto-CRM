from time import sleep
from colors import c
from base_crud import GestorCRUD, GestorDB

class Proveedor:
    def __init__(self, nombre_proveedor):
        nombre_proveedor = nombre_proveedor.strip()
        if not nombre_proveedor:
            raise ValueError("Nombre incorrecto!")        
        else:
            self.nombre_proveedor = nombre_proveedor

class GestorProveedores(GestorCRUD, GestorDB):
    def __init__(self):
        self.lista_proveedores = []

    def _buscar_posicion(self, id):
        # * Obtener el indice de lista proveedores
        for i in range(len(self.lista_proveedores)):
            if self.lista_proveedores[i]["id"] == id:
                return i
        return -1

    def _obtener_último_id(self):
        if bool(self.lista_proveedores):
            lista_invertida = self.lista_proveedores[::-1]
            ultimo_id = lista_invertida[0]["id"]
            ultimo_id += 1 # * Aumentando el valor de ID
            return ultimo_id
        else:
            ultimo_id = 1
            return ultimo_id

    def _crear_proveedor(self):
        ultimo_id = self._obtener_último_id()
        nombre_proveedor = input(f"Ingresar nombre proveedor: ")
        proveedor = Proveedor(nombre_proveedor)
        nuevo_proveedor = {"id": ultimo_id, "nombre_proveedor": proveedor.nombre_proveedor}
        
        return nuevo_proveedor
    
    # -----------------------
    # * CRUD de Proveedores
    # -----------------------
    def crear(self):
        nuevo_proveedor = self._crear_proveedor()

        if nuevo_proveedor:
            self.lista_proveedores.append(nuevo_proveedor)
            print(f"{c.GREEN}[+] Proveedor creado{c.END}\n")
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
