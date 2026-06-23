from abc import ABC, abstractmethod

# 1. Definimos una interfaz base abstracta
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


# 2. Implementamos el Rectángulo
class Rectangulo(Forma):
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self) -> float:
        return self.ancho * self.alto


# 3. Implementamos el Cuadrado de forma independiente
class Cuadrado(Forma):
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado


# Función que espera una 'Forma' (Cumple con LSP)
def imprimir_area(forma: Forma):
    print(f"El área es: {forma.calcular_area()}")


# Uso
mi_rectangulo = Rectangulo(4, 5)
mi_cuadrado = Cuadrado(4)

imprimir_area(mi_rectangulo)  # Salida: El área es: 20
imprimir_area(mi_cuadrado)  # Salida: El área es: 16
