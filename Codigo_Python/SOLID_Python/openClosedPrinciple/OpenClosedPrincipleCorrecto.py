from abc import ABC, abstractmethod

# 1. Clase base cerrada a modificaciones
class Descuento(ABC):
    @abstractmethod
    def aplicar(self, monto: float) -> float:
        pass

# 2. Extensiones abiertas para nuevos tipos
class DescuentoNavidad(Descuento):
    def aplicar(self, monto: float) -> float:
        return monto * 0.20

class DescuentoAniversario(Descuento):
    def aplicar(self, monto: float) -> float:
        return monto * 0.15

class DescuentoVIP(Descuento):
    def aplicar(self, monto: float) -> float:
        return monto * 0.30

class SinDescuento(Descuento):
    def aplicar(self, monto: float) -> float:
        return monto

# 3. Calculadora que NO necesita ser modificada si agregas un nuevo descuento
class CalculadoraDescuentos:
    def calcular(self, monto: float, estrategia_descuento: Descuento) -> float:
        return estrategia_descuento.aplicar(monto)

# Uso
monto_final = CalculadoraDescuentos().calcular(100.0, DescuentoNavidad())
