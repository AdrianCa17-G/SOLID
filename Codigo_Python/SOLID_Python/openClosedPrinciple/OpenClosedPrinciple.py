class CalculadoraDescuentos:
    def calcular(self, monto, tipo_descuento):
        if tipo_descuento == "navidad":
            return monto * 0.20
        elif tipo_descuento == "aniversario":
            return monto * 0.15
        elif tipo_descuento == "vip":
            return monto * 0.30
        return monto
