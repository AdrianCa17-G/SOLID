/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package openClosedPrinciple;

/**
 *
 * @author SALASC
 */
public class OpenClosedPrinciple {

    public class CalculadoraDescuento {

        public double calcular(double monto, String tipoCliente) {
            if (tipoCliente.equals("REGULAR")) {
                return monto * 0.10;
            } else if (tipoCliente.equals("PREMIUM")) {
                return monto * 0.20;
            }
            return 0;
        }
    }

}
