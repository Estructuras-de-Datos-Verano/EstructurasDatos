# Catalogo de patrones - Clase 08

Nombre: Leonardo Daniel Arenas Serafín

## Patron 1: Simulacion

- Problema ejemplo: Simular el funcionamiento de un editor de texto, un cajero, un juego de cartas, etc.
- Pregunta detonadora: ¿El problema consiste en ejecutar paso a paso una serie de instrucciones exactamente como se describen?
- Estructuras que suelen aparecer: Listas, pilas, colas, diccionarios, matrices.
- Ejemplo en clase: Simular el historial de un navegador usando una pila
- Cuando usarlo: Cuando el problema necesita solamente seguir una serie de instrucciones para realizar una actividad o llevar acabo un proceso
- Cuando no usarlo: Cuando existe una solución matemática o un algoritmo más eficiente

## Patron 2: Informacion monotonica

- Problema ejemplo: Encontrar el nearest smaller/greater, máximos en una slide window o calcular cuántos días faltan para una temperatura mayor por ejemplo
- Pregunta detonadora: ¿Necesito mantener los elementos ordenados mientras recorro el arreglo para responder consultas rápidamente?
- Estructuras que suelen aparecer: pilas y colas
- Ejemplo en clase: Usamos las pilas para resolver un problema de sintáxis matemático de paréntesis, corchetes y llaves
- Cuando usarlo: Cuando es necesario llevar un orden en los extremos de un arreglo
- Cuando no usarlo: Cuando queremos acceder a la información que está en el medio del arreglo

## Patron 3: Árboles

- Problema ejemplo: Recorrer un árbol binario para encontrar un valor, calcular la altura del árbol o verificar si un árbol está balanceado.
- Pregunta detonadora: ¿Los datos tienen una estructura jerárquica donde cada elemento depende de otro?
- Estructuras que suelen aparecer: árboles binarios, n-arios, colas
- Ejemplo en clase o recurso consultado: no han havido ejemplos
- Cuando usarlo: cuando queremos llevar una estrategia de retroceso, cuandon quieres conocer todos los posibles caminos y llevar un orden jerárquico
- Cuando no usarlo: cuando no hay una secuencia clara y solo son datos almacenados

## Patron 4: Heaps 

- Problema ejemplo: Encontrar rápidamente el elemento mínimo o máximo, administrar una cola de prioridad o calcular los k elementos más grandes o más pequeños.
- Pregunta detonadora:¿Necesito obtener repetidamente el elemento con mayor o menor prioridad de forma eficiente?
- Estructuras que suelen aparecer: cola de prioridad
- Ejemplo en clase o recurso consultado: creo que no han habido ejemplos 
- Cuando usarlo: cuando se quiere mantener el orden de elementos agregados y poder acceder al mínimo o máximo fácilmente 
- Cuando no usarlo: cuando es necesario mantener uun orden estricto para acceder a cualquier dato

## Comparacion breve

#### Árboles y Heaps

- Se parecen en que ambos tienen una cierta noción de jerarquía, de secuencia y de orden, la diferencia es que los heaps mantienen un orden lineal y los árboles tienen un orden ramificado

## Pregunta abierta

#### Que patron te parece mas dificil de reconocer antes de escribir codigo?

- Las pilas, pues no son tan intuitivas en ciertos casos
