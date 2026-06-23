from abc import ABC, abstractmethod

# Interfaces pequeñas y específicas
class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


# Implementación de las clases
class Car(Drivable):
    def drive(self):
        print("Conduciendo el auto...")


class Airplane(Drivable, Flyable):
    def drive(self):
        print("Rodando en la pista...")

    def fly(self):
        print("Volando en el cielo...")


class Drone(Flyable):
    def fly(self):
        print("Drone volando...")
