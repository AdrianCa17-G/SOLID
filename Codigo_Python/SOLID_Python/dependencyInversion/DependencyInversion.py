class PasarelaPayPal:
    def procesar_pago(self, monto: float):
        print(f"Procesando pago de ${monto} a través de PayPal.")

class Pedido:
    def __init__(self, monto: float):
        self.monto = monto
        # Dependencia directa de una implementación concreta
        self.pasarela = PasarelaPayPal()

    def confirmar(self):
        self.pasarela.procesar_pago(self.monto)

# Uso
pedido = Pedido(150.0)
pedido.confirmar()
