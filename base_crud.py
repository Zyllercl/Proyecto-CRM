from abc import ABC, abstractmethod

class GestorCRUD(ABC):
    @abstractmethod
    def crear(self):
        pass
     
    @abstractmethod
    def leer(self):
        pass

    @abstractmethod
    def actualizar(self):
        pass

    @abstractmethod
    def eliminar(self):
        pass

class GestorDB(ABC):
    @abstractmethod
    def total_lista(self):
        pass

    @abstractmethod
    def buscar_por_id(self):
        pass