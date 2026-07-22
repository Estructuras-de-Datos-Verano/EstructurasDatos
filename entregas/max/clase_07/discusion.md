# 1. Problema y primera idea.
Crear un código que pueda leer una lista y decirnos cual es el valor izquierdo menor más cercano, indexandols pero desde el 1 a diferencia de desde el cero como lo hacen las lista habituales.

# 2. Por qué la solución ingenua repite trabajo.
Por que va comparando uno a uno cada elemento con el que tiene a la izquirda y haciendolo en tuplas que no se pueden modificar, entonces a la hora de querer leer un dato dos posiciones a la izquierda de nuestro pivote necesita crear otra tupla y repetir el procedimiento hasta llegar a la ultima tupla de la izquierda, por lo que poco eficiente.

# 3. Información útil e información descartable.
La información descartable es la pocisión de los elementos iniciales, ya que esta se va a cambiar para empezar desde uno en lugar desde cero, ahora la información util sera conservar nuestra posición para que así se puedan compara bien el valor de los elementos de la izquierda de nuestro pivote.

# 4. Elección de estructura.
La elección de estructura para resolver este problema realmente es bastante sencilla, y es la de un deque, así podemos ir modificando tanto la cola como la cima.

# 5. Variante: Nearest Greater Values.
Es exactamente la misma estructura, unicamnete cmabiando el mayor igual por un menor igual.

# 6. Contraejemplo: Maximum Subarray Sum.
Acá hay buscar la mayor suma posible de un subconjunto que este conectado del mismo conjunto.

# 7. Sliding Window.
Acá hay un poco más de structura en la implementación, porque para empezar, de fondo tenemos una nueva variable, que es el numero de subconjuntos necesarios, luego hay que crearlos de manera connectada, osea que no haya subcoonjuntos con huecos entre los vlores y luego acomodarlos de menor a mayos para sacar su mediana, y así sacar la mayor suba dentro de los subconjuntos.

# 8. Invariante.
Lo que no cambia es el orden y los valores de la lista originalmente ingresada

# 9. Pruebas.
Se probaron que todas las funciones funcionen correctamente

# 10. Complejidad.
Se probo que la complejidad no cambia cuando se busca el valor más chico o más grande del conjunto y se demostro que la complejidad en el peor ecseenario es cuadratica.

# 11. Cómo descubrimos el algoritmo.
Lo fuimos construyencdo poco a poco desglosanso el problema en partes y ejemplos más sencillos, hast que llegamos a implementar una lgoritmo que puesa solucionar todos los casos de manera general.

# 12. Pregunta abierta.
¿Se pueden ocupar sets para resolver este tipo de problemas?
No, ya que dets tiene dos caracteristicas que nos pejudican que nos que pierden el orden y que quitan valores repetidos, así que en estricto sentido no son conjuntos en toda la definición formal de la palabra
