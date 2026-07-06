### Discusión Técnica
---
        Gustavo Torres
---

## 1. Lectura estratégica.

    El problema pide simular un proceso iterativo en un círculo formado por $n$ niños. Se debe aplicar estrictamente la regla de "saltar a un niño (salvarlo) y eliminar al siguiente", repitiendo este ciclo ininterrumpidamente hasta que no quede nadie. El objetivo final es devolver una lista que contenga los números de los niños en el orden exacto en el que fueron eliminados.

## 2. Elección de estructura.

    ¿Por qué una cola? Porque el problema requiere procesar elementos en un orden cíclico continuo (FIFO modificado). Una cola permite extraer al elemento del frente y reinsertarlo al final en tiempo constante, lo cual es la abstracción perfecta para simular la rotación de un círculo.

    ¿Qué otra estructura consideraste?Consideré usar una lista tradicional y también evalué estructuras.

    ¿Por qué las descartaste?Descarté la lista tradicional porque eliminar elementos de su inicio con pop(0) obliga a desplazar todos los demás elementos en la memoria, tomando un tiempo O(n) por operación y volviendo todo el algoritmo. 

## 3. Diseño del algoritmo.

    1. Comenzamos llenando una cola con los números del$1 al n.
    2. Iniciamos un bucle que continuará mientras la cola no esté vacía.
    3. Fase de Salto: Si hay más de un niño en la cola, tomamos al primero, lo sacamos de la fila y lo volvemos a formar al final. Esto simula que sobrevivió al turno.
    4. Fase de Eliminación: Tomamos al niño que ahora está al frente de la cola, lo sacamos permanentemente y anotamos su número en nuestra lista de resultados.
    5. El ciclo se repite hasta que el último niño se desencola y se añade al resultado.

## 4. Pruebas.

    Si tomamos orden.eliminación(7)  debe regresar [2, 4, 6, 1, 5, 3, 7]. Esta prueba verifica que el algoritmo maneje correctamente las "vueltas" al círculo. Después de eliminar al 6, el círculo se reinicia, demostrando que el enlace entre el final y el principio funciona y que el niño 1 es el siguiente en caer. También verifica que el último sobreviviente (el 7) sea extraído correctamente al final.

## 5. Complejidad.

    Para vaciar una cola de $n$ niños, realizamos como máximo un "salto" (desencolar y encolar) y una "eliminación" (desencolar) por niño. El uso adicional de memoria consta de la cola inicial (deque) que almacena n elementos.

## 6. Contraste.

    Depende enteramente del cambio. Si el problema se convierte en el "Josephus Problem II", donde en lugar de saltar a 1 niño, tienes que saltar a K niños (y K puede ser un número enorme, como 10^9), no seguiría usando una cola.  Porque con una cola, simular un salto de tamaño $k$ requiere hacer el proceso de "sacar y poner al final" $k$ veces seguidas antes de poder eliminar a uno solo

## 7. Pregunta abierta.

    Cada vez que un niño es eliminado, el círculo se encoge de n a n-1 personas y la cuenta continúa de inmediato desde el niño que sobrevivió al lado del eliminado.Conceptualmente, si pausamos el juego en ese exacto momento e ignoramos a la persona que acaba de salir, ¿podríamos afirmar que estamos ante un juego de Josefo completamente nuevo e independiente, solo que con diferentes "etiquetas" en los asientos?

---

### Complejidad

## ¿Cuántos niños se eliminan?

    Se eliminan n niños. Aunque el problema histórico de Josefo se centra en encontrar al único sobreviviente, esta variante de programación te pide el orden completo en el que la ronda se vacía. El último niño también es extraído de la cola y agregado a la lista de resultados al final.

## ¿Cuántas veces se mueve o procesa cada niño?

    El número de veces que se procesa a un niño individual depende de cuánto tiempo logre sobrevivir:Los que son eliminados en la primera ronda se procesan solo 1 vez. El último sobreviviente se procesa múltiples veces, ya que debe dar varias vueltas al círculo antes de quedar solo. Sin embargo, si miramos el sistema completo, cada ciclo del bucle hace exactamente dos operaciones: salva a uno y elimina a otro. 

## ¿Qué estructura permite que esas operaciones sean eficientes?

    Por Deque el bucle de "sacar del frente y poner al final" se ejecuta a la máxima velocidad posible de la computadora sin desperdiciar recursos acomodando datos.

## ¿Cuánta memoria adicional se usa?

    El algoritmo utiliza una memoria adicional. Esto se debe a que la memoria crece de manera directamente proporcional a la cantidad de niños. 
