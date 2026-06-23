/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package liskovSubstitutionPrinciple;

/**
 *
 * @author SALASC
 */
public class LiskovSubstitutionPrinciple {

    class Ave {

        public void volar() {
            System.out.println("El ave está volando");
        }
    }

    class Gorrión extends Ave {
        // Hereda volar() sin problemas
    }

    class Pingüino extends Ave {

        @Override
        public void volar() {
            // VIOLACIÓN DE LSP: Los pingüinos no vuelan, esto genera un error de lógica
            throw new UnsupportedOperationException("Los pingüinos no pueden volar");
        }
    }

}
