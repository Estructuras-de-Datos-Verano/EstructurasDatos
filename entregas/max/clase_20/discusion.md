# Discusión técnica — Clase 20

Nombre: Max

## Escenario 1

- Problema y objetivo: Un circuito de calles dentro de una ciudad
- Dirección y pesos: Bidireccional y puede costar 1 o 0
- Operación dominante: Continuar en el camino
- Estructura y algoritmo: Dijsktra
- Contrato: Continuar o no en el camino
- Alternativa descartada: Los minutos no negativos
- Módulo previo reutilizado: El modulo de la coneción de ciudades supongo
- Adaptación de entrada/salida: tener que ver el peso de 0 y 1
- Prueba distintiva: la prueba de ver si si vota de manera correcta los resultados cuando hay valores diferentes
- Complejidad e interpretación: Logaritmico

## Escenario 2

- Problema y objetivo: Conectar enlaces entre edificios
- Dirección y pesos: No tiene dirección ni costo
- Operación dominante: Checar si los edificios ya estan conectados
- Estructura y algoritmo: Va a ser del tipo
- Contrato: Union_find
- Alternativa descartada: Kruskal
- Módulo previo reutilizado: El modulo de las clases anteriores
- Adaptación de entrada/salida: hay que adaptar la falta de peso en el algoritmo
- Prueba distintiva: ver que pasa si un edificio esta desconectado
- Complejidad e interpretación: logaritmica

## Caso fuera del alcance

Los casos fuera del alcanse de este tipo de programas son los que llegan a ser ciclicos, ya qu en estos casos no tendremos una solución concreta

## Reflexión final

Cambio de una manera bastante positiva ya que ahora ya soy capaz de visualizar los problemas de una manera más concreta y profunda