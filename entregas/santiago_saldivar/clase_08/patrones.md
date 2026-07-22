# Catalogo de patrones - Clase 08

Nombre: Santiago Saldívar Garcini

## Patron 1: Simulacion

- Problema ejemplo: Guardar operaciones en un editor de texto.
- Pregunta detonadora: ¿Cómo registro las acciones del usuario?
- Estructuras que suelen aparecer: Pilas.
- Ejemplo en clase: Los historiales de búsqueda.
- Cuando usarlo: Cuando se necesita acceder al elemento agregado más recientemente.
- Cuando no usarlo: Cuando se necesita preservar el orden por antigüedad.

## Patron 2: Informacion monotonica

- Problema ejemplo: Nearest Smaller Values
- Pregunta detonadora: ¿Cómo registro los valores menores sin tener que volver a revisar todos los datos?
- Estructuras que suelen aparecer: Pila
- Ejemplo en clase: Nearest Smaller Values
- Cuando usarlo: Cuando voy iterando y guardo los valores más útiles.
- Cuando no usarlo: Cuando hacemos el Maximum Subarray Sum

## Patron 3: Flujo de tareas

- Problema ejemplo: Seguir una serie de pasos en secuencia.
- Pregunta detonadora:¿Cómo garantizo que se siga un orden específico?
- Estructuras que suelen aparecer: Linked Lists.
- Ejemplo en clase o recurso consultado: Una receta que requiere un orden.
- Cuando usarlo: Cuando es especialmente importante que se avance en una dirección.
- Cuando no usarlo: Cuando necesito poder acceder a cualquier dato.

## Patron 4: Ordenamiento

- Problema ejemplo: Necesito encontrar el mínimo de una función en varios momentos.
- Pregunta detonadora: ¿Cómo garantizo que la operación devuelva el número que busco?
- Estructuras que suelen aparecer: Priority Queue
- Ejemplo en clase o recurso consultado: Encontrar el número más chico de una lista que se va actualizando.
- Cuando usarlo: Cuando no importa en qué momento entro cada elemento, sino la relación entre ellos.
- Cuando no usarlo: Cuando la antigüedad de un elemento es especialmente relevante.

## Patrones adicionales opcionales

Puedes agregar mas patrones si tus recursos te llevaron a ellos.

## Comparacion breve

Escoge dos patrones y explica en que se parecen y en que se diferencian.

- Ordenamiento y Flujo de tareas

Similitudes: Ambos trabajan con varios datos que se relacionan entre sí de cierta forma jerárquica. 

Diferencias: En el caso del ordenamiento, trabaja con propiedes internas que deben ser comparables dato con dato. En el otro, el orden está dado por el objeto mismo, no es especialmente relevante qué atributos exactamente tenga cada dato.

## Pregunta abierta

Que patron te parece mas dificil de reconocer antes de escribir codigo?

- EL 4, ordenamiento.
