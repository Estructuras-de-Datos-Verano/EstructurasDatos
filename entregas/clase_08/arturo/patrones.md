# Catalogo de patrones - Clase 08

Nombre: Arturo Prudencio Bonilla

## Patron 1: Simulacion

- Problema ejemplo: El problema de Josephus, donde un grupo de elementos en un círculo se elimina de forma secuencial.
- Pregunta detonadora: 
- Estructuras que suelen aparecer: Colas, arreglos, y ciclos (while/for).
- Ejemplo en clase: Utilizar una cola (queue) para extraer un elemento y volver a insertarlo al final si no debe ser eliminado (simulación del problema de Josephus).
- Cuando usarlo: Cuando las reglas del problema dictan pasos deterministas y es necesario observar o almacenar los estados intermedios del sistema.
- Cuando no usarlo: Cuando los límites del problema ($N$) son masivos y existe una fórmula matemática cerrada que resuelve el estado final directamente.

## Patron 2: Informacion monotonica

- Problema ejemplo: Nearest Smaller Values
- Pregunta detonadora: ¿Necesito encontrar el siguiente o anterior elemento que sea mayor/menor bajo una condición de orden estricto?
- Estructuras que suelen aparecer: Pilas (Monotonic Stacks).
- Ejemplo en clase: Mantener una pila creciente para resolver Nearest Smaller Values, eliminando los elementos que dejan de ser útiles.  
- Cuando usarlo: En problemas de rangos, histogramas o subarreglos donde la relación de orden (mayor/menor) descarta candidatos inútiles de forma definitiva, optimizando el tiempo a lineal 
- Cuando no usarlo: Cuando la búsqueda de elementos no depende de un orden relativo estricto o cuando los datos no tienen un patrón de monotonicidad

## Patron 3:

- Problema ejemplo: Encontrar dos números en un arreglo ordenado que sumen un valor objetivo (Two Sum II)
- Pregunta detonadora: ¿El problema implica iterar sobre una secuencia ordenada o buscar pares/elementos en los extremos que se acercan al centro?
- Estructuras que suelen aparecer: Arreglos ordenados, listas doblemente ligadas
- Ejemplo en clase o recurso consultado: Buscar un palíndromo en una cadena usando un puntero al inicio y otro al final
- Cuando usarlo: Cuando se neccesita optimizar la búsqueda de pares o subarrays en una estructura lineal ordenada para reducir la complejidad temporal
- Cuando no usarlo: Cuando el arreglo no está ordenado (y no se puede ordenar sin perder la referencia) o si el problema requiere un historial profundo de estados

## Patron 4:

- Problema ejemplo: Encontrar la suma máxima de un subarreglo contiguo de tamaño K
- Pregunta detonadora: ¿El problema pide optimizar (maximizar/minimizar) un subarreglo o subsecuencia contigua bajo una restricción específica 
- Estructuras que suelen aparecer: Arreglos, cadenas de texto (strings), diccionarios/Hash Maps para contar frecuencias
- Ejemplo en clase o recurso consultado: Mantener una suma local agregando el elemento entrante por la derecha y restando el elemento saliente por la izquierda
- Cuando usarlo: Cuando se analizan subarreglos contiguos y existe superposición de cálculos entre ventanas adyacente 
- Cuando no usarlo: Cuando los elementos a agrupar no son contiguos (subsecuencias en lugar de subarreglos)

## Patrones adicionales opcionales

Búsqueda Binaria (Binary Search): Útil para buscar en espacios de respuestas monótonos o arreglos ordenados, dividiendo el espacio de búsqueda a la mitad.

## Comparacion breve

Escoge dos patrones y explica en que se parecen y en que se diferencian.

- Dos punteros y Ventana Deslizante: Ambos optimizan problemas de arreglos recorriéndolos en tiempo lineal. La diferencia es que Dos punteros generalmente opera reduciendo el espacio desde los extremos hacia el centro (o procesando dos arreglos), mientras que la Ventana deslizante evalúa un bloque contiguo fijo o dinámico que avanza en una sola dirección.

## Pregunta abierta

Que patron te parece mas dificil de reconocer antes de escribir codigo?

- El patrón de Información monotónica es el más difícil de identificar intuitivamente.
