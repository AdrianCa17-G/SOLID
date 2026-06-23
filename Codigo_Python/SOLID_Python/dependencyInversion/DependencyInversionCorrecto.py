from abc import ABC, abstractmethod

# Abstracción (Interfaz)
class PasarelaPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float):
        pass

# Implementación de bajo nivel 1
class PasarelaPayPal(PasarelaPago):
    def procesar_pago(self, monto: float):
        print(f"Procesando pago de ${monto} a través de PayPal.")

# Implementación de bajo nivel 2 (Se puede agregar sin modificar Pedido)
class PasarelaStripe(PasarelaPago):
    def procesar_pago(self, monto: float):
        print(f"Procesando pago de ${monto} a través de Stripe.")

# Módulo de alto nivel
class Pedido:
    def __init__(self, monto: float, pasarela: PasarelaPago):
        self.monto = monto
        # Depende de la abstracción, no de la implementación
        self.pasarela = pasarela

    def confirmar(self):
        self.pasarela.procesar_pago(self.monto)

# Uso
pago_paypal = PasarelaPayPal()
pedido_1 = Pedido(150.0, pago_paypal)
pedido_1.confirmar()

pago_stripe = PasarelaStripe()
pedido_2 = Pedido(200.0, pago_stripe)
pedido_2.confirmar()
