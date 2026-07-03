# Clase 07 discusión - Leonardo Daniel Arenas Serafín

## 1. Problema y primera idea.
El problema es el de nearest smaller. Lo que se pide es que dada una lista de enteros, por cada elemento se compare con sus anteriores a la izquierda para encontrar cuál es el número menor más próximo, para despues regresar una lista de cuáles son las posiciones de estos números menores más próximos para cada elemento de la lista original.

## 2. Por qué la solución ingenua repite trabajo.
Porque tiene que comparar todo los elementos uno por uno por cada iteración de la lista y no es eficiente

## 3. Información útil e información descartable.
La información útil es cuáles son los números que son menores a otros que ya aparecieron anteriormente a la izquierda. La información descartable son aquellos números que a su derecha (antes de llegar al elemento que está siendo evaluado en la iteración) tienen números menores a ellos, lo que signfica que al comparar, el algoritmo nunca llegará a ellos, pues hay menores que se compararán primero.

## 4. Elección de estructura.
Se eligió la pila pues es una estructura que mantiene el orden de una lista de ir de izqueirda a derecha y va comparando con los más próximos al solamente poder trabajar con los últimos elementos agregados

## 5. Variante: Nearest Greater Values.
Es exactamente el mismo algoritmo, la única mínima diferencia es que a la hora de descartar elementos de la pila, en vez de usar un `>=` se usa un `<=`.

## 6. Contraejemplo: Maximum Subarray Sum.
En este contraejemplo considero que no debe ser útil usar la pila, pues la pila mantiene un orden semejante al de la lista de ir de izquierda a derecha lo cual ayuda a mantener el elemento "más cercano". Sin embargo para este caso, no hay un criterio que establezca cuál es el orden, pues aquí estamos trabajando con subconjuntos y no con números.

## 7. Sliding Window.
Todo cambia completamente, las posiciones, los valores, las listas. Todo se vuelve mucho más complejo y parece ser que las pilas no son una opción. Yo considero que podría ser muy útil usar diccionarios aquí, pues a cada llave le puedes asignar una posición y le metes los valores que ocupan esa posición por cada iteración.

## 8. Invariante.
Lo que es invariante es que siempre cuando la pila esté vacía, aparecerá un "0" como respuesta. A causa de esto, el primer elemento de la lista de respuestas siempre sera "0"

## 9. Pruebas.
Teníamos ya implementadas 3 pruebas y yo implementé 6 más: test_todo_valores_iguales, test_todo_error_comparacion_estricta, test_todo_caso_limite, test_todo_variante_nearest_greater, test_LEO_concavidad, test_LEO_convexidad. Aquellas que tienen mi nombre son pruebas que yo creé desde cero. En cambio las que no, solamente son pruebas que completé. Estas pruebas fueron muy útiles para poder verificar que nuestro algoritmo funciona correctamente en cualquier situación y que siempre marca errores.

## 10. Complejidad.
La complejidad de la implementación ingenua y más natural es cuadrática. Sin embargo, cuando hacemos el algoritmo con pilas, la complejidad se vuelve lineal, pues siempre se compara uno a uno y nada más.

## 11. Cómo descubrimos el algoritmo.
Lo descubrimos haciendo un análisis profundo de qué es lo que nos pide el problema, qué tipo de herramientas tenemos, cómo podríamos implementarlas. Descubrimos qué tipo de información sería descartable y cuál sería candidata útil a conservar, logramos optimizar el proceso de elección de menores y posteriormente planteando un pseudocódigo que sería nuestra guía para diseñar finalmente el algoritmo

## 12. Pregunta abierta.
#### Todo es muy fácil cuando lo hacemos de izquierda a derecha pues ese es el orden natural de los arreglos. Sin embargo, ¿qué pasaría si en vez de encontrar el menor valor más próximo a la izquierda lo hicieramos hacia la derecha?
Considero que para resolver esto bastaría simplemente con darle la vuelta a lista con comandos que ya conocemos para posteriormente utilizar el mismo algoritmo que se usa para hacerlo por la izquierda. Para finalmente, a cada posición en vez de solo guardarla, deberíamos de restársela al valor de la longitud de la lista original y esa sería la verdadera posición.