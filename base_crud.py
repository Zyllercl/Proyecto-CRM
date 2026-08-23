from abc import ABC, abstractmethod

class GestorCRUD(ABC):
    def __init__(self, titulo=" - "):
        self.titulo = titulo

    @abstractmethod
    def crear(self):
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
    def buscar(self):
        pass