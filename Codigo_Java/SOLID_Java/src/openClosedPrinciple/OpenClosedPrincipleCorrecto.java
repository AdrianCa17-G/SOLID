/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package openClosedPrinciple;

/**
 *
 * @author SALASC
 */
public class OpenClosedPrincipleCorrecto {

    // 1. Interfaz común
    public interface Descuento {

        double calcular(double monto);
    }

// 2. Extensión para clientes regulares
    public class DescuentoRegular implements Descuento {

        @Override
        public double calcular(double monto) {
            return monto * 0.10;
        }
    }

// 3. Extensión para clientes premium
    public class DescuentoPremium implements Descuento {

        @Override
        public double calcular(double monto) {
            return monto * 0.20;
        }
    }

// 4. Clase principal (Cerrada a modificaciones)
    public class CalculadoraDescuento {

        public double procesarDescuento(Descuento tipoDescuento, double monto) {
            return tipoDescuento.calcular(monto);
        }
    }

}
