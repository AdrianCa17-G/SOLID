/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package liskovSubstitutionPrinciple;

/**
 *
 * @author SALASC
 */
public class liskovSubstitutionPrincipleCorrecto {
    // 1. Abstracción base

    interface Ave {

        void comer();
    }

// 2. Abstracción específica para aves que vuelan
    interface AveVoladora {

        void volar();
    }

// 3. Implementaciones concretas
    class Gorrión implements Ave, AveVoladora {

        @Override
        public void comer() {
            System.out.println("El gorrión está comiendo");
        }

        @Override
        public void volar() {
            System.out.println("El gorrión está volando");
        }
    }

    class Pingüino implements Ave {

        @Override
        public void comer() {
            System.out.println("El pingüino está comiendo");
        }
        // Ya no tiene el método volar() que lo obligaría a fallar
    }

}
