# Catalogo de patrones - Clase 08

Nombre:

## Patron 1: Simulacion

- Problema ejemplo: El problema del recurso 8 (Wrong Subtraction),
- Pregunta detonadora: ¿El problema me da un conjunto de reglas e instrucciones explícitas paso a paso sobre cómo cambia un estado a lo largo del tiempo?
- Estructuras que suelen aparecer: for, while, deque
- Ejemplo en clase: o vimos ningun ejemplo en clse
- Cuando usarlo: Cuando lqa complejidad del problema seapequeña
- Cuando no usarlo:Cuando la complejidad crezca

## Patron 2: Informacion monotonica

- Problema ejemplo: El ejemplo del recurso 7 de tirar un huevo en un edificio de 100 pisos
- Pregunta detonadora: ¿Las respuestas posibles o los datos de entrada tienen una propiedad de ordenamiento?
- Estructuras que suelen aparecer: Areglos, lisztas
- Ejemplo en clase: o vimos ningn ejemplo en clse
- Cuando usarlo: : Cuando el espacio de búsqueda es gigantesco pero está estrictamente ordenado
- Cuando no usarlo: Cuando los datos no esten ordenados

## Patron 3:

- Problema ejemplo: Prefix sums
- Pregunta detonadora: ¿Necesito calcular propiedades de subarreglos o rangos?
- Estructuras que suelen aparecer: Prefix arrays
- Ejemplo en clase: o vimos ningun ejemo en clse
- Cuando usarlo: Yo evitaria usarlo en genral
- Cuando no usarlo: En particular cuando no cambian sus valores en medio de la estructura

## Patron 4:

- Problema ejemplo: cuando necesite procesar de mayor/menor prioridad
- Pregunta detonadora: ¿El problema requiere que extraiga constantemente el elemento mínimo o máximo?
- Estructuras que suelen aparecer: heapq
- Ejemplo en clase: o vimos nigun ejemplo en clse
- Cuando usarlo: Cuando la lista de datos cambia constantemente de tamaño
- Cuando no usarlo: Cuando la lsita se permanece constante

## Patrones adicionales opcionales

No tengo

## Comparacion breve

Escoge dos patrones y explica en que se parecen y en que se diferencian.

- El patron 1 y los , y ya los compare en la refelxión

## Pregunta abierta

Que patron te parece mas dificil de reconocer antes de escribir codigo?

- Prefix sums, de plano no lo usaria
