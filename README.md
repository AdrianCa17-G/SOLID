# SOLID — Principios de Diseño Orientado a Objetos

Ejemplos prácticos de los 5 principios SOLID aplicados en **Java** y **Python**, mostrando en cada caso el código que viola el principio y la solución correcta.

---

## SOLID EN JAVA

---

### 1. Single Responsibility Principle — SRP
> *"Una clase debe tener una sola razón para cambiar."*

#### Código Incorrecto (Viola el principio)
Aquí, la clase `Factura` asume tres responsabilidades distintas: calcular el total, guardar en la base de datos e imprimir el documento.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Java/SJava.png" alt="Texto alternativo" width="700"/>

#### Código Correcto (Aplica el principio)
Para aplicar el SRP, dividimos la clase original en tres clases separadas, donde cada una se encarga de una sola tarea.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Java/SCJava.png" alt="Texto alternativo" width="700"/>

---

### 2. Open-Closed Principle — OCP
> *"El software debe estar abierto para extensión, pero cerrado para modificación."*

#### Código Incorrecto (Viola el principio)
Si usas un bloque `if-else` o `switch`, cada vez que agregues un tipo de cliente nuevo (ej. `ClienteVIP`), tendrás que modificar la clase existente, lo que rompe el principio y aumenta el riesgo de errores.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Java/OJava.png" alt="Texto alternativo" width="700"/>

#### Código Correcto (Aplica el principio)
Creas una interfaz `Descuento` y una clase separada para cada tipo de cliente. La clase `CalculadoraDescuento` queda cerrada a modificaciones y el sistema queda abierto a extensiones (solo creas una nueva clase que implemente la interfaz).

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Java/OCJava.png" alt="Texto alternativo" width="700"/>

---

### 3. Liskov Substitution Principle — LSP
> *"Las subclases deben poder sustituir a su clase base sin alterar el comportamiento del programa."*

#### Código Incorrecto (Viola el principio)
Un ejemplo clásico es el de un ave. Si creas una clase `Ave` con un método `volar()`, los pájaros (como un `Gorrión`) funcionarán bien. Sin embargo, si creas un `Pingüino` que hereda de `Ave`, este no puede volar. Para que el programa no falle, la clase `Pingüino` se ve obligada a lanzar una excepción (`UnsupportedOperationException`), violando así el LSP.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Java/LJava.png" alt="Texto alternativo" width="700"/>

#### Código Correcto (Aplica el principio)
Para cumplir con el LSP, debes separar las capacidades en interfaces o clases base más específicas, de modo que solo las clases que verdaderamente puedan realizar la acción implementen ese comportamiento.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Java/LCJava.png" alt="Texto alternativo" width="700"/>

---

### 4. Interface Segregation Principle — ISP
> *"Ninguna clase debe verse obligada a implementar métodos que no usa."*

#### Código Incorrecto (Viola el principio)
Supongamos que creamos una interfaz para trabajadores con diferentes responsabilidades. Si implementamos un `Robot` usando esta interfaz, tenemos un problema: el robot no come, pero está obligado a implementar el método, lo que genera código basura o excepciones.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Java/IJava.png" alt="Texto alternativo" width="700"/>

#### Código Correcto (Aplica el principio)
Para aplicar el principio correctamente, dividimos la interfaz `Trabajador` en interfaces más pequeñas y cohesivas. Ahora, tanto el `Robot` como un `Humano` implementan únicamente las interfaces que les corresponden.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Java/ICJava.png" alt="Texto alternativo" width="700"/>

---

### 5. Dependency Inversion Principle — DIP
> *"Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones."*

#### Código Incorrecto (Viola el principio)
En este ejemplo, la clase de alto nivel `Notificador` tiene una dependencia directa de la clase de bajo nivel `Email`. Si en el futuro quieres enviar mensajes por SMS o WhatsApp, tendrás que modificar el código de `Notificador`.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Java/DJava.png" alt="Texto alternativo" width="700"/>

#### Código Correcto (Aplica el principio)
Para cumplir con el principio, creamos una interfaz (abstracción) llamada `Mensajero`. Ahora, `Notificador` dependerá de esta interfaz, y cualquier clase que envíe mensajes la implementará.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Java/DCJava.png" alt="Texto alternativo" width="700"/>

---

## SOLID EN PYTHON

---

### 1. Single Responsibility Principle — SRP
> *"Una clase debe tener una sola razón para cambiar."*

#### Código Incorrecto (Viola el principio)
En este caso, la clase `Factura` hace demasiadas cosas: calcula el total, genera el reporte y guarda el archivo. Si cambian los requisitos de cómo se guarda el archivo o cómo se imprime, tendrías que modificar esta clase.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Python/SPython.png" alt="Texto alternativo" width="700"/>

#### Código Correcto (Aplica el principio)
Para cumplir con el SRP, separamos las responsabilidades en clases independientes. Ahora `Factura` solo maneja los datos y el cálculo, `GeneradorReporte` se encarga de la salida visual, y `GestorFactura` administra el almacenamiento.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Python/SCPython.png" alt="Texto alternativo" width="700"/>

---

### 2. Open-Closed Principle — OCP
> *"El software debe estar abierto para extensión, pero cerrado para modificación."*

#### Código Incorrecto (Viola el principio)
Aquí, cada vez que hay un tipo de descuento nuevo, estás obligado a modificar la clase `CalculadoraDescuentos` agregando otro `if`. Esto viola el principio, ya que el código original no está cerrado a la modificación.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Python/SPython.png" alt="Texto alternativo" width="700"/>

#### Código Correcto (Aplica el principio)
Se utiliza polimorfismo. Creamos una clase base y extendemos el sistema mediante nuevas subclases, sin modificar jamás la clase que maneja el cálculo principal.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Python/SPython.png" alt="Texto alternativo" width="700"/>

---

### 3. Liskov Substitution Principle — LSP
> *"Las subclases deben poder sustituir a su clase base sin alterar el comportamiento del programa."*

#### Código Incorrecto (Viola el principio)
Un error común es intentar que un cuadrado herede de un rectángulo. Matemáticamente un cuadrado es un rectángulo, pero en programación esto suele romper la regla de sustitución, porque las variables de ancho y alto de un rectángulo cambian de forma independiente, mientras que en un cuadrado no.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Python/SPython.png" alt="Texto alternativo" width="700"/>

#### Código Correcto (Aplica el principio)
Para cumplir con el LSP, ambos deben derivar de una interfaz base más genérica (como `Forma`), y cada clase debe implementar su propia lógica sin alterar las expectativas de la otra.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Python/SPython.png" alt="Texto alternativo" width="700"/>

---

### 4. Interface Segregation Principle — ISP
> *"Ninguna clase debe verse obligada a implementar métodos que no usa."*

#### Código Incorrecto (Viola el principio)
Un `Car` (automóvil) se ve obligado a implementar el método `fly()` (volar), lo cual no tiene sentido y provoca código basura.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Python/SPython.png" alt="Texto alternativo" width="700"/>

#### Código Correcto (Aplica el principio)
Separamos la interfaz general en dos más pequeñas (`Drivable` y `Flyable`). Ahora cada vehículo implementa únicamente el contrato que le corresponde.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Python/SPython.png" alt="Texto alternativo" width="700"/>

---

### 5. Dependency Inversion Principle — DIP
> *"Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones."*

#### Código Incorrecto (Viola el principio)
En este ejemplo, la clase de alto nivel `Pedido` crea directamente una instancia de la clase de bajo nivel `PasarelaPayPal`. Si en el futuro necesitas cambiar a Stripe, tendrás que modificar el código interno de `Pedido`, lo que viola el principio.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Python/SPython.png" alt="Texto alternativo" width="700"/>

#### Código Correcto (Aplica el principio)
Para aplicar el DIP, introducimos una abstracción (`PasarelaPago`) y utilizamos la inyección de dependencias para pasar la pasarela deseada al instanciar `Pedido`. Ahora `Pedido` depende de una abstracción y no de los detalles de bajo nivel.

<img src="https://github.com/AdrianCa17-G/SOLID/blob/main/Imagenes_Python/SPython.png" alt="Texto alternativo" width="700"/>
