class Factura:
    """Responsabilidad única: Almacenar los datos de la factura y calcular su total."""
    def __init__(self, cliente, monto, impuesto):
        self.cliente = cliente
        self.monto = monto
        self.impuesto = impuesto

    def calcular_total(self):
        return self.monto + self.impuesto


class GeneradorReporte:
    """Responsabilidad única: Dar formato a la factura para visualizarla o imprimirla."""
    @staticmethod
    def generar_pdf(factura):
        return f"--- PDF ---\nFactura de {factura.cliente}\nTotal: {factura.calcular_total()}"


class GestorFactura:
    """Responsabilidad única: Guardar la factura en el sistema de archivos."""
    @staticmethod
    def guardar_en_disco(factura, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            contenido = GeneradorReporte.generar_pdf(factura)
            archivo.write(contenido)


# Uso del código
mi_factura = Factura(cliente="Juan Pérez", monto=100.0, impuesto=12.0)
GestorFactura.guardar_en_disco(mi_factura, "factura_001.txt")
