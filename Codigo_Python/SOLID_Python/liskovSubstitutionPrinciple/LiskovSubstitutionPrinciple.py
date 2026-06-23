class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def set_ancho(self, ancho):
        self.ancho = ancho
        self.alto = ancho  # Modificar ambos lados para mantener la forma
