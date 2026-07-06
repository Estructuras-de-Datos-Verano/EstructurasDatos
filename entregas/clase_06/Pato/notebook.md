# Clase 06: Notebook
#### Nombre: Patricio Navarro

## Entrada, salida y restricciones

Completa en tu copia del notebook:

```text
Entrada:
- Un entero n, para el numero de niños.

Salida:
- El órden en que salen los niños del círculo

Restricción principal:
- 1 <= n <= 2*(10^5)
```

Dato importante del enunciado: `1 <= n <= 2 * 10^5`.

Eso significa que una solución demasiado lenta puede fallar aunque sea correcta en ejemplos pequeños.

## Ingeniería inversa del algoritmo

Esta sección será permanente en las siguientes clases.

Antes de escribir una sola línea de código, responde:

1. ¿Qué está pidiendo exactamente el problema?
    - Que demos el órden en el que los niños saldrán del círculo.
2. ¿Qué información debo recordar mientras avanzo?
    - Los niños que ya salieron, el órden en que salieron, los que quedan, en donde están del círculo. 
3. ¿Qué operaciones realizo continuamente?
    - Búsqueda y eliminación.
4. ¿Existe una estructura de datos que implemente naturalmente esas operaciones?
    - Las colas, pilas, listas.
5. ¿Cómo resolvería este problema con papel y lápiz?
    - Con combinatoria. De los n niños, tomo 1, quedan 6 y tomo otro, y me quedaria que es n! la forma de elegir el órden en que salen los niños.

## Preguntas de modelado

Responde antes de seguir:

1. Cuando un niño se salva, ¿desaparece del problema?
    - No, sigue estando en el círculo por lo que se sigue considerando.
2. Cuando un niño se elimina, ¿vuelve a participar?
    - No, una vez que salen ya no se pueden volver a unir al círculo.
3. ¿Qué significa avanzar en un círculo si estamos usando una estructura lineal?
    - Recorrerse una posición a un punto de inicio que nosotros elegimos.
4. ¿Qué operación se repite una y otra vez?
    - Búsqueda y eliminación, encolar o apilar.

## Diseñar el algoritmo en español

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

```text
Tenemos una cola con n niños. 
Lo anterior respeta la regla de eliminar uno de cada dos porque toma un punto arbitrario de partida que convenientemente es la cabeza de la cola.
Toma a la cabeza y al niño que le sigue y de esos dos elimina a 1. 
A manera de ruleta se recorren las posiciones de los niños, asi el niño que se salvo queda al final, y se toma a la siguiente pareja.
Se repite hasta que solo queda un niño, por lo que ese niño es último eliminado.
```

## Pseudocódigo

Completa los espacios marcados:

```text
función orden_eliminacion(n):
    validar n
    vivos = cola con números de 1 a n
    eliminados = lista vacía

    mientras vivos no esté vacía:
        si solo queda un niño:
            eliminarlo y guardarlo
        si no:
            TODO: mover al final al niño que se salva
            tomar a la cabeza y guardarla al final de la cola
            TODO: eliminar al siguiente niño
            tomar otra vez a la cabeza de la cola después de guardar al pasado y guardarla en una variable de paso
            TODO: guardar el eliminado
            añadir este niño eliminado a la lista de eliminados a traves de la variable de paso

    regresar eliminados
```

Hay varias formas de escribirlo. Lo importante es que cada operación tenga sentido en el modelo.

## Cierre

Preguntas de contraste para discutir:

1. Si se eliminara cada tercer niño, ¿la cola seguiría siendo natural?
    * Sí, solo cambiaría la cantidad de veces que hicimos las operacines, pero de primeras me parece un caso casi análogo.
2. Si necesitáramos consultar siempre el menor número vivo, ¿la cola bastaría?
    * Sí, podrías nada más verificar cuantos elementos siguen en ella con `tamano()`
3. Si el círculo cambiara dinámicamente con inserciones en medio, ¿qué parte del modelo se rompería?
    * Se rompería la implementación de la cola yo creo, porque ya no tendría un comportamiento FIFO, habría niños en medio que ya fueron eliminados, que se repiten y que además se eliminan antes que los que ya estaban.
4. ¿Qué prueba pública te da más confianza y cuál falta?
    * La del ejemplo oficial, pero sí creo que faltan los casos para n muy grande y para una n que excede el límite superior.