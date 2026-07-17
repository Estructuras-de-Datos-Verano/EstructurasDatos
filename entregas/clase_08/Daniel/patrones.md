# Catalogo de patrones - Clase 08

Nombre: José Daniel Molina Carrillo

## Patron 1: Simulacion

- Problema ejemplo: Un robot recibe una lista de movimientos y debemos simular su posicion en un tablero de 5x5.
- Pregunta detonadora: ¿Qué pasa si procesamos los movimientos uno por uno en orden?
- Estructuras que suelen aparecer: lista, cola, diccionario.
- Ejemplo en clase: Simular una fila de clientes en una tienda usando una cola FIFO.
- Cuando usarlo: Cuando el problema pide ejecutar pasos en orden y llevar un estado.
- Cuando no usarlo: Cuando la respuesta se puede obtener con una formula directa o con una sola observacion.

## Patron 2: Informacion monotonica

- Problema ejemplo: En un sistema de monitoreo, cada minuto se registra el nivel de agua y queremos encontrar el primer momento en que deja de bajar.
- Pregunta detonadora: ¿La secuencia de datos siempre avanza en una sola direccion?
- Estructuras que suelen aparecer: pila, lista, deque.
- Ejemplo en clase: Mantener una pila de alturas y descartar las que ya no pueden ser solucion.
- Cuando usarlo: Cuando los datos pueden compararse con un valor anterior y el resultado se mantiene ordenado.
- Cuando no usarlo: Cuando la relacion entre elementos cambia de forma compleja y no hay un orden creciente o decreciente.

## Patron 3: Dos punteros

- Problema ejemplo: En un almacen inventado, tenemos una lista de cajas con pesos y queremos encontrar dos cajas que sumen un valor objetivo.
- Pregunta detonadora: ¿Podemos reducir la busqueda usando los extremos de la estructura?
- Estructuras que suelen aparecer: lista, arreglo, deque.
- Ejemplo en clase o recurso consultado: Usar dos punteros para encontrar un par de valores en una lista ordenada.
- Cuando usarlo: Cuando necesitamos comparar elementos opuestos o buscar en una estructura ordenada sin revisar todo.
- Cuando no usarlo: Cuando los datos no estan ordenados o el problema requiere varias condiciones complejas.

## Patron 4: Hashing o tabla de frecuencia

- Problema ejemplo: En una biblioteca inventada, cada libro tiene un codigo y queremos saber si un codigo ya fue registrado.
- Pregunta detonadora: ¿Necesitamos consultar rapidamente si un elemento ya existe o cuantas veces aparece?
- Estructuras que suelen aparecer: conjunto, diccionario, tabla hash.
- Ejemplo en clase o recurso consultado: Guardar nombres de alumnos en un diccionario para verificar duplicados.
- Cuando usarlo: Cuando el acceso rapido a un valor es mas importante que mantener el orden.
- Cuando no usarlo: Cuando necesitamos recorrer datos en orden o buscar por rango.

## Patrones adicionales opcionales

- Busqueda binaria: util cuando la respuesta tiene un rango ordenado y se puede descartar la mitad de las opciones.

## Comparacion breve

Escoge dos patrones y explica en que se parecen y en que se diferencian.

- Simulacion e informacion monotonica se parecen porque ambos recorren datos paso a paso. Se diferencian porque la simulacion sigue el flujo del problema, mientras que la informacion monotonica aprovecha que los datos tienen un orden.

## Pregunta abierta

Que patron te parece mas dificil de reconocer antes de escribir codigo?

- Me parece mas dificil reconocer la informacion monotonica, porque a veces el problema no muestra claramente que los datos pueden organizarse en orden.
