from abc import ABC, abstractmethod

# Interfaz genérica y demasiado grande (Viola el ISP)
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Conduciendo el auto...")

    def fly(self):
        # ¡Un auto no puede volar! Esto es un problema de diseño.
        raise NotImplementedError("Los autos no vuelan.")
