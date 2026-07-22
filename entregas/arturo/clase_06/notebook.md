# Clase 06 - Arturo Prudencio Bonilla

## Ingeniería inversa del algoritmo
1. ¿Qué está pidiendo exactamente el problema?
    - un algoritmo que dado un numero natural pueda arrogarte (tras un procedimiento) una lista de eleemtnos eliminados bajos ciertas circusntacnias
2. ¿Qué información debo recordar mientras avanzo?
    - las restriccines, la entrada y la salida
3. ¿Qué operaciones realizo continuamente?
    - agregar a una lista y quitar de otra
4. ¿Existe una estructura de datos que implemente naturalmente esas operaciones?
    - PILA o COLA 
5. ¿Cómo resolvería este problema con papel y lápiz?
    - no se
6. Escribir únicamente después el pseudocódigo.

## Modelado
1. Cuando un niño se salva, ¿desaparece del problema?
    - no
2. Cuando un niño se elimina, ¿vuelve a participar?
    - no 
3. ¿Qué significa avanzar en un círculo si estamos usando una estructura lineal?
    - que cuando pasas el "final" regras al inicio
4. ¿Qué operación se repite una y otra vez?
    - agregar y eliminar de listas 

## Diseñar el algortimo en español
```text
Crear una cola con los niños del 1 al n.
Mientras haya niños vivos:
    mover al final al niño que se salva
    eliminar al siguiente niño
    guardar el eliminado en la respuesta
Regresar la respuesta
```

Explicacion de porque funciona: porque siempre se garantiza que de lso dos niños que estan al inicio del circulo, uno se salva y se va al final y el otro se elimina

### Pseudocodigo
```text
función orden_eliminacion(n):
    validar n
    vivos = cola con números de 1 a n
    eliminados = lista vacía

    mientras vivos no esté vacía:
        si solo queda un niño:
            eliminarlo y guardarlo
        si no:
            mover al final al niño que se salva
            eliminar al siguiente niño
            guardar el eliminado en eliminados

    regresar eliminados
```


## Cierre


1. Si se eliminara cada tercer niño, ¿la cola seguiría siendo natural?
    - Si, pues no dejamos de hacer las mismas dos operaciones nativas de la cola
2. Si nesitáramos consultar siempre el menor número vivo, ¿la cola bastaría?
    - no seimpre, pues despues del primer paso, el menor numero vivo estara al final de la cola
3. Si el círculo cambiara dinámicamente con inserciones en medio, ¿qué parte del modelo se rompería?
    - no piesno que el modelo se romperia realmente, no puedo pensar en ningun problema realmente
4. ¿Qué prueba pública te da más confianza y cuál falta?
    - la mas sencilla (el caso minimo) y creo que falta una prueba como la extra que yo puse, que para numeros grandes el comportamiento del algortimo se mantiene