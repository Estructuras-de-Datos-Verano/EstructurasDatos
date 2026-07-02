### Entrada, salida y restricciones

Completa en tu copia del notebook:

Entrada:
- Un entero n, que representa la cantidad de niños.

Salida:
- El número del niño que permanece al final después de eliminar
  repetidamente a uno de cada dos.

Restricción principal:
- 1 <= n <= 2 * 10^5.
- La solución debe ser eficiente, evitando simulaciones con
  operaciones costosas sobre arreglos o listas.

Dato importante del enunciado: `1 <= n <= 2 * 10^5`.

Eso significa que una solución demasiado lenta puede fallar aunque sea correcta en ejemplos pequeños.

---

# Ingeniería inversa del algoritmo

Esta sección será permanente en las siguientes clases.

Antes de escribir una sola línea de código, responde:

1. ¿Qué está pidiendo exactamente el problema?

***Pues que en "n" niños, 1 de cada 2 serán eliminados, con orden en la salida, todo esto modelado, estructurado y programado en una implementación eficiente***

2. ¿Qué información debo recordar mientras avanzo?

***Las condiciones y las definiciones del problema***

3. ¿Qué operaciones realizo continuamente?

***Encolar, desencolar, esta_vacia, frente, tamaño, assert, etc.***

4. ¿Existe una estructura de datos que implemente naturalmente esas operaciones?

***Sí. las colas FIFO***

5. ¿Cómo resolvería este problema con papel y lápiz?

***Podría hacer un diagrama de flujo que explique puntualmente las operaciones y resultados esperados, hasta que concluye en la resolución deseada.***

6. Escribir únicamente después el pseudocódigo.

Mientras el tamaño de la cola sea mayor que 1

    niño_restante ← Desencolar()
    Encolar(niño_restante)

    niño_eliminado ← Desencolar()
    Mostrar eliminado (opcional)

FinMientras

Mostrar el único elemento restante

---

### Preguntas de modelado

1. Cuando un niño se salva, ¿desaparece del problema?

***No, ya que continúa participando, por lo que debe volver al final de la cola.***

2. Cuando un niño se elimina, ¿vuelve a participar?

***Tampoco, sale definitivamente del juego y no vuelve a encolarse.***

3. ¿Qué significa avanzar en un círculo si estamos usando una estructura lineal?

***Significa que el niño que está al frente y se salva se mueve al final de la cola, simulando el recorrido circular sin necesidad de una estructura circular.***

4. ¿Qué operación se repite una y otra vez?

Mientras haya más de un niño:
- El primero se salva y pasa al final de la cola.
- El siguiente es eliminado.
- El proceso se repite hasta que quede un único niño.

---


## 4. Diseñar el algoritmo en español

Antes del pseudocódigo, escríbelo en lenguaje natural.

Una versión posible es:

```text
Crear una cola con los niños del 1 al n.
Mientras haya niños vivos:
    mover al final al niño que se salva
    eliminar al siguiente niño
    guardar el eliminado en la respuesta
Regresar la respuesta
```

Ahora explica con tus palabras por qué esto respeta la regla de eliminar uno de cada dos.


***El algoritmo respeta la regla porque en cada iteración siempre ocurren dos acciones en el mismo orden. Primero, el niño que está al frente de la cola se salva y se coloca al final, manteniendo su participación en el juego. Después, el siguiente niño que queda al frente es eliminado definitivamente. Al repetir este proceso, siempre se conserva el patrón de "uno se salva y el siguiente se elimina", lo que equivale a eliminar uno de cada dos niños hasta que solo quede uno.***

---

## Pseudocódigo

Completa los espacios marcados:


función orden_eliminacion(n):
    validar n
    vivos = cola con números de 1 a n
    eliminados = lista vacía

    mientras vivos no esté vacía:
         si tamaño(vivos) == 1:
            eliminado = desencolar(vivos)
            agregar eliminado a eliminados

        si no:
            sobreviviente = desencolar(vivos)
            encolar(vivos, sobreviviente)

            eliminado = desencolar(vivos)
            agregar eliminado a eliminados

    regresar eliminados




