### Entrada, salida y restricciones

Completa en tu copia del notebook:

```text
Entrada:
n

Salida:
orden de eliminación
Restricción principal:
1 <= n <= 2 * 10^5
```

Dato importante del enunciado: `1 <= n <= 2 * 10^5`.


# Ingeniería inversa del algoritmo

Esta sección será permanente en las siguientes clases.

Antes de escribir una sola línea de código, responde:

1. ¿Qué está pidiendo exactamente el problema?

 El orden de eliminación de los niños.

2. ¿Qué información debo recordar mientras avanzo?

 La entrada y las reglas para eliminar a los niños.

3. ¿Qué operaciones realizo continuamente?

Eliminar a algún niño del círculo y salvarlo.

4. ¿Existe una estructura de datos que implemente naturalmente esas operaciones?

No que yo sepa.

5. ¿Cómo resolvería este problema con papel y lápiz?

Podríamos dibujar el círculo e ir eliminando.

6. Escribir únicamente después el pseudocódigo.

Escrito más adelante.


### Preguntas de modelado

Responde antes de seguir:

1. Cuando un niño se salva, ¿desaparece del problema?

No.

2. Cuando un niño se elimina, ¿vuelve a participar?

No durante ese mismo problema. Sólo si se vuelve a iniciar.

3. ¿Qué significa avanzar en un círculo si estamos usando una estructura lineal?

Que del último volvemos al primero.

4. ¿Qué operación se repite una y otra vez?

La de eliminar y salvar a los niños.


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

## Respuesta

La respeta porque trabaja con los dos primeros niños: al primero lo salva y lo guarda al final, al segundo lo elimina. Sigue haciendo esto mientras haya niños vivos. Entonces, a cada niño eliminado, le sigue uno salvado, porque así comienza el siguiente paso. 

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
            eliminar al niño
            agregarlo al final de vivos
            eliminar el siguiente
            agregarlo a eliminados

    regresar eliminados
```

Hay varias formas de escribirlo. Lo importante es que cada operación tenga sentido en el modelo.

## Cierre

Preguntas de contraste para discutir:

1. Si se eliminara cada tercer niño, ¿la cola seguiría siendo natural?

Sí, porque seguimos trabajando igual, sólo agregando una salvada más.

2. Si necesitáramos consultar siempre el menor número vivo, ¿la cola bastaría?

No necesariamente, porque a veces no queda en orden ascendente tras varias eliminaciones y salvadas.

3. Si el círculo cambiara dinámicamente con inserciones en medio, ¿qué parte del modelo se rompería?

La lista de vivos porque actualmente no contempla inserciones que no sean una salvada al final.

4. ¿Qué prueba pública te da más confianza y cuál falta?

Falta la de los casos más grandes. Me da confianza la que valida n, porque eso es la base del modelo.