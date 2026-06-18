## Actividad de proyecto / Github 


## Nombre

Santiago Vázquez Serna 

## Definición propia de TDA

"Contrato" de un conjunto de datos y las operaciones que puedes hacer con ellos.

## Diferencia entre interfaz e implementación 

Interfaz:

Es la parte visible simplificada de la interacción de las operaciones con esos datos.

Implementación:

La realización ó "backstage" de la propia interfaz

## Problema donde usarías una pila

Navegación en navegadores

## Propuesta de interfaz para pila 

Operaciones:

-push(elemento): agrega un elemento del tope

-pop(): elimina y regresa el elemento del tope

-peek(): regresa el elemento del tope sin eliminarlo

-esta_vacia(): Valor de verdad en los dif. casos

-tamano(): todos los elementos

## Prueba mínima en lenguaje natural 


Prueba mínima:

Si apilo 1 y luego 2, entonces pop debe regresar 2.
Si apilo 1 y luego 2, entonces peek debe regresar 2 sin eliminarlo.
Una pila recién creada debe estar vacía.
Si hago pop sobre una pila vacía, debe lanzar una excepción (por ejemplo EmptyStackError o IndexError).
Si hago peek sobre una pila vacía, debe lanzar una excepción.
Si apilo X y luego hago pop, el valor devuelto debe ser X.
Si apilo A, B, C en ese orden, tres pops consecutivos deben devolver C, B, A.




**ningun cambio, todo bien** 