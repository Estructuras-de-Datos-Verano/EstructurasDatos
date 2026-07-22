### Discusión

El problema es encontrar el número menor más cercano a la izquierda de cada número en la lsita, y retornar una lista con sus posiciones. Inmediatamente nos viene una idea muy intuitiva a la cabeza: todos contra todos. Comparar cada número con todos os previos y guardar el que funcione. Esta solución ingenua repetirá mucho trabajo, porque hace comparaciones de más. Es mejor trabajar con la pila, donde guardaremos las posiciones de un tope, que le meteremos a la pila según iteremos sobre la lista. Las comparaciones redundantes son completamente descartables y no hacen sino entorpecer el algortimo.

Como se dijo ya, la pila resulta una estructura óptima para este problema. Según vayamos iterando, guardaremos en esta pila los valores y sus posiciones. La pila es clave porque, si el valor previo al que nos compete en cada iteración no es el que ha de guardarse, lo eliminamos de la pila, le hacemos pop. 

La variante de Nearest Greater Values es, en esencia, lo mismo. Sólo eliminamos de la pila los valores menores o iguales, en vez de mayores o iguales. Para el Maximum Subarray Sum una pila podría servir, ya que podemos ir guardando las sumas, y eliminando las que sean superadas. Para el sliding window, funciona similar. Según se mueva la ventana, tendremos que agregar y eliminar elementos. 

Las pruebas son bastante intuitivas, sólo hay que confirmar que el algoritmo esté registrando correctamente las posiciones. Por ejemplo, dando listas de 0 en casos crecientes, o dando listas de números consecutivos en el caso contrario. 

La complejidad aumentará cuadráticamente en el peor de los casos, porque acabaremos agregando muchas cosas a la pila según iteremos, y por cada n serán n.

Descubrimos el algoritmo con ayuda del Profe, preguntándonos cómo mantener sólo la información útil.

### Pregunta abierta

¿Qué problemas así existen para el resto de estructuras de datos?