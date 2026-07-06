# Sección 1 (Lectura estrategica)

Tipo de datos de entrada y de salida, incluyendo restricciones

```text
Entrada:

    Numero de niños que estan el circulo (tiene que ser un número entero) Aun uqe más adelante en los ejemplos tambien se pide el número de pasos para las rondas de eliminación, siento que este pedimento es opcional realmente, ya que realmente lo podriamos correr hasta que se acaben todos los niños

Salida:

    Orden en que se fueron eliminando los niños

Restricción principal:

    La eliminación de niños se tiene que realizar cada dos niños, es decir uno si uno no, respetando el hecho que estan en un circulo, o sea como lo vimos el semestre pasado con graficas, los niños se comportan como si fueran un anillo

```
## Sección 1.2 (Ingenieria inversa del algoritmo)

1. ¿Qué está pidiendo exactamente el problema?

    Lo que nos esta pidiendo realmente es un algoritmo que trage listas y escupa listas, que utilizando pilas, reacomode la lista inicial en lo que sera la lista final en la cual se estaran acomodando a los niños en el orden en el que se fueron eliminando.

2. ¿Qué información debo recordar mientras avanzo?

    Debo de recordar que niños siguen vivos, cuales ya "fallecieron" y el orden el que estan los niños, o mejor dicho el nuevo orden, cuando menciono esto del nuevo orden ya hace sentido el porque unicamente podemos correr los datos hasta un cierto número antes de perden el control del codigo, porque recordemos que al pensarlo con pilas cuando estados añadiendo o eliminando elementos lo que realmente estamos haciendo es que estamos reacomodando toda la lista, como que la estamos volviendo a indexar, y es por eso que a partir de un punto muy grande esto se rompe.

3. ¿Qué operaciones realizo continuamente?

    Claramente, estamos en la nececidad de acupar una pila de tipo deque, porque así podemos modificar la cola para darle este efecto "circular", entonces lo que estaremos ocupando continuamente es el .popleft y el .append tanto para modificar la lista restante, como ara crear la nueva reacomodada.

4. ¿Existe una estructura de datos que implemente naturalmente esas operaciones?

    Desconozco si exista ya una especie de plantilla previa donde podemos moldear lo que necesitamos pero supongo que si

5. ¿Cómo resolvería este problema con papel y lápiz?

    Utilizando graficas (Las que supuestamente vimos en matemáticas discretas), en las cuales iremeos eliminando participantes hastaquedarnos con 0, y lo iremos anotando en una especie de tabla donde este pueste el numero de rondas y el participante eliminado

# Sección 2 (Modelado)

1. Cuando un niño se salva, ¿desaparece del problema?

    No, cuando un niño se salva vuelve a la lista de participantes vivos, peo un nuelo lugar, que en este caso sera el lugar de hatsa la derecha y esto representa que se le dio la vuelta al circulo, pero todos siguen participando.

2. Cuando un niño se elimina, ¿vuelve a participar?

    En este caso no, cuando un niño se elimina se sale de la lista (pila) actual para entrar a la nuev lista de candidatos eliminados

3. ¿Qué significa avanzar en un círculo si estamos usando una estructura lineal?

    La representación de darle la vuelta la lista y volver a la posición original es la de recorrer la pila en el nuevo orden sin los jugadores ya eliminados y los salvados ya reacomodados.

4. ¿Qué operación se repite una y otra vez?

    .popleft y .append

# Sección 4 (Diseñar el algoritmo en español)

¿Porque en el código funciona que se eliminen cada dos niños?

```text
Como ya lo vimos en los ejemplos y ya explique un poco más a fondo en las secciones pasadas lo que hace que erespete este orden circular e ignore el orden lineal es que constantemente los datos se estan recorriento en la lista en un mismo sntido, pensemos este tipo de reordenamiento como una banda en una cinta transportadora, donde la banda en ralidad es una linea recta, pero como esta girando continuamente en una misma dirección podriamos pensar que si dibujamos un punto en esta banda, este rotara al redodor de ella como si se tratara de un circulo y no una recta. De una manera similar se comportan estas listas en las cuales el reodenamiento se comporta como un circulo, luego si a este pseudocirculo le agregamos instrucciones para saltarse a uno y eliminar a otro es por eso que se elimina cada dos.

```

## Sección 4.2 (Pseudocódigo)

```text
función orden_eliminacion(n):
    validar n   # O sea que n si sea un número natural
    vivos = cola con números de 1 a n
    eliminados = lista vacía

    mientras vivos no esté vacía:
        si solo queda un niño:
            eliminarlo y guardarlo
        si no:
            vivos += el niño actual movido hasta al frente
            eliminados += el niño actual            # Ojo que este "niño actual" es diferente el que se agrego a vivos
            vivos = vivos menos el niño acual       # Ojo que este "niño actual" es el mismol que se agrego a eliminados

    regresar eliminados
```


