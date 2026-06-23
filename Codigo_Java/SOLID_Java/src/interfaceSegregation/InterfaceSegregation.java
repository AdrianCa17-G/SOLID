/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package interfaceSegregation;

/**
 *
 * @author SALASC
 */
public class InterfaceSegregation {

    public interface Trabajador {

        void trabajar();

        void comer();

        void programar();
    }

    public class Robot implements Trabajador {

        @Override
        public void trabajar() {
            System.out.println("Robot trabajando...");
        }

        @Override
        public void comer() {
            // Violación del principio: Un robot no come
            throw new UnsupportedOperationException("Operación no soportada");
        }

        @Override
        public void programar() {
            System.out.println("Robot programando...");
        }
    }

}
