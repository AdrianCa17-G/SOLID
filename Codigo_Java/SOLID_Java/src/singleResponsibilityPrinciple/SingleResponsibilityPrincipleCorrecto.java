package singleResponsibilityPrinciple;

public class SingleResponsibilityPrincipleCorrecto {

    public class Factura {

        // Clase 1: Solo calcula el total
        public class CalculadoraFactura {

            public void calcularTotal() {
                // Lógica para calcular el importe total
            }
        }

// Clase 2: Solo maneja el almacenamiento
        public class RepositorioFactura {

            public void guardarEnBaseDeDatos() {
                // Lógica para conectar y guardar en la BD
            }
        }

// Clase 3: Solo se encarga de la impresión
        public class ImpresorFactura {

            public void imprimirFactura() {
                // Lógica para enviar a la impresora
            }
        }

    }

}
