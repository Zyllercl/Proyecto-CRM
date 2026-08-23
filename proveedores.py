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
        self.lista_proveedores = [
            {"id": 1, "nombre_proveedor": "Lays"},
            {"id": 2, "nombre_proveedor": "Fruna"},
            {"id": 3, "nombre_proveedor": "Evercrisp"},
            {"id": 4, "nombre_proveedor": "San Jorge"},
        ]
        super().__init__("Proveedores")

    def _buscar_posicion(self, buscar_nombre):       
        # * Obtener el indice de lista proveedores
        for i in range(len(self.lista_proveedores)):
            if self.lista_proveedores[i]["nombre_proveedor"].strip().lower() == buscar_nombre.strip().lower():
                return i
        raise ValueError("Proveedor no existe!")

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
        nombre_proveedor = input(f"[CREATE] Ingresar nombre proveedor: ")
        proveedor = Proveedor(nombre_proveedor)
        existe_proveedor = self._existe_proveedor(proveedor.nombre_proveedor)

        if existe_proveedor:
            raise ValueError("El proveedor ya existe!")
        else:
            nuevo_proveedor = {"id": ultimo_id, "nombre_proveedor": proveedor.nombre_proveedor}
            return nuevo_proveedor

    def _existe_proveedor(self, nombre):
        try:
            self._buscar_posicion(nombre)
            return True
        except ValueError:
            return False
    
    # -----------------------
    # * CRUD de Proveedores
    # -----------------------
    def crear(self):
        nuevo_proveedor = self._crear_proveedor()

        if nuevo_proveedor:
            self.lista_proveedores.append(nuevo_proveedor)
            print(f"{c.GREEN}[+] Proveedor creado{c.END}")
            sleep(0.5)

    def actualizar(self):
        self.total_lista()
        buscar_proveedor = input(f"\n[UPDATE] Ingrese proveedor: ")
        buscar_posicion = self._buscar_posicion(buscar_proveedor)

        nuevo_nombre = input("[UPDATE] Ingrese nuevo nombre: ")
        proveedor_actualizado = Proveedor(nuevo_nombre)

        self.lista_proveedores[buscar_posicion]["nombre_proveedor"] = proveedor_actualizado.nombre_proveedor
        print(f"{c.GREEN}[+] Proveedor actualizado{c.END}")

    def eliminar(self):
        self.total_lista()
        buscar_proveedor = input(f"\n[DELETE] Ingrese proveedor: ")
        posicion = self._buscar_posicion(buscar_proveedor)

        del self.lista_proveedores[posicion]
        print(f"[DELETE] Proveedor eliminado con éxito!")
    
    def buscar(self):
        buscar_proveedor = input(f"\n[SEARCH] Buscar proveedor: ")
        posicion = self._buscar_posicion(buscar_proveedor)

        print(f"[INFO] Nombre: {self.lista_proveedores[posicion]["nombre_proveedor"]}\n")

    def total_lista(self):
        if (bool(self.lista_proveedores)):
            print(f"Total Proveedores {len(self.lista_proveedores)}: {self.lista_proveedores}")
        else:
            print(f"{c.RED}[!] No hay proveedores.{c.END}")
