/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dependencyInversion;

/**
 *
 * @author SALASC
 */
public class DependencyInversion {
    // Módulo de bajo nivel (concreto)

    public class Email {

        public void enviarMensaje(String mensaje) {
            System.out.println("Enviando email: " + mensaje);
        }
    }

// Módulo de alto nivel
    public class Notificador {

        private Email email;

        public Notificador() {
            // Acoplamiento fuerte: Dependemos de la implementación concreta
            this.email = new Email();
        }

        public void enviar(String mensaje) {
            email.enviarMensaje(mensaje);
        }
    }

}
