class Factura:
    def __init__(self, cliente, monto, impuesto):
        self.cliente = cliente
        self.monto = monto
        self.impuesto = impuesto

    def calcular_total(self):
        return self.monto + self.impuesto

    def generar_reporte(self):
        # Responsabilidad de presentación
        return f"Factura de {self.cliente} - Total: {self.calcular_total()}"

    def guardar_en_disco(self, nombre_archivo):
        # Responsabilidad de persistencia / almacenamiento
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(self.generar_reporte())
