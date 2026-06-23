/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package interfaceSegregation;

/**
 *
 * @author SALASC
 */
public class InterfaceSegregationCorrecto {

    // Interfaz específica para acciones de trabajo
    public interface Trabajable {

        void trabajar();
    }

// Interfaz específica para la pausa de almuerzo
    public interface Comestible {

        void comer();
    }

// Interfaz específica para tareas de software
    public interface Programable {

        void programar();
    }

    public class Robot implements Trabajable, Programable {

        @Override
        public void trabajar() {
            System.out.println("Robot trabajando...");
        }

        @Override
        public void programar() {
            System.out.println("Robot programando...");
        }
    }

    public class Humano implements Trabajable, Comestible, Programable {

        @Override
        public void trabajar() {
            System.out.println("Humano trabajando...");
        }

        @Override
        public void comer() {
            System.out.println("Humano comiendo...");
        }

        @Override
        public void programar() {
            System.out.println("Humano programando...");
        }
    }

}
