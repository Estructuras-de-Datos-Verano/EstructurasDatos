# Notebook - Clase 09

## 1. Problemas motivadores CSES
**Pregunta.** ¿Qué diferencia hay entre modelar una secuencia y modelar relaciones? Una secuencia tiene por dominio enteros positivos mientras que una relación entre dos cosas pude tener por dominio cualquier otro conjunto. Esto hace que simular una relación cualesquiera exija pensar también en un "paso", en vez de solo usar unidades de tiempo.
## 2. Modelado de relaciones
### Building Roads
1. ¿Qué representa un nodo? Una ciudad.
2. ¿Qué representa una arista? Una carretetera entre (estrictamente) dos ciudades.
3. ¿Es dirigido? No, podría ir en dos sentidos. 
4. ¿Es ponderado? No.
5. ¿Qué pregunta algorítmica aparece? ¿Cómo relaciono los elementos de una estrctura de datos dos a dos minimizando la cantidad de relaciones?
### Counting Rooms
1. ¿Qué representa un nodo? Un cuarto.
2. ¿Qué representa una arista? Cuartos contiguos (separados por solo una pared).
3. ¿Es dirigido? No.
4. ¿Es ponderado? No.
5. ¿Qué pregunta algorítmica aparece? ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula y contar ciertos espacios de interés?
### Labyrinth
1. ¿Qué representa un nodo? Puntos en una cuadrícula.
2. ¿Qué representa una arista? Un camino entre dos puntos en la cuadícula.
3. ¿Es dirigido? Sí, es necesario asumir que vas estrictamente de "A" a "B" ya que ir al revés te devuelve al inicio del laberinto. 
4. ¿Es ponderado? No, aumque los pesos a cada forna de llegar se pueden asignar según la longitud de pasos. En este caso preferimos un peso pequeño.
5. ¿Qué pregunta algorítmica aparece? ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula de múltiples formas posibles sin incrementar mucho la cpmplejidad?
### Message Route
1. ¿Qué representa un nodo? Una computadora.
2. ¿Qué representa una arista? Una conexión (biunívoca) entre dos computadoras distintas.
3. ¿Es dirigido? Sí, es necesario asumir que vas estrictamente de "A" a "B" ya que ir al revés te devuelve al remitente. 
4. ¿Es ponderado? No, aunque los pesos a cada forna enviar el mensaje se pueden asignar según la longitud de la red de conexiones. En este caso preferimos un peso pequeño.
5. ¿Qué pregunta algorítmica aparece? ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula de múltiples formas posibles sin incrementar mucho la cpmplejidad?
| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | Ciudad | Carretera | No | No | ¿Cómo relaciono los elementos de una estrctura de datos dos a dos minimizando la cantidad de relaciones? |
| Counting Rooms | Cuarto  | Cuartos contiguos | No | No | ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula y contar ciertos espacios de interés? |
| Labyrinth | Puntos (plano coordenado) | Camino entre dos puntos | Sí | No | ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula de múltiples formas posibles sin incrementar mucho la cpmplejidad? |
| Message Route | Computadora | Conexión(biunívoca) | Sí | No | ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula de múltiples formas posibles sin incrementar mucho la cpmplejidad? |
## 3. Conceptos básicos de grafos
**Pregunta.** Da un ejemplo propio de grafo dirigido y otro de grafo no dirigido.
- Dirigido: Formas de llegar de una ciudad A a B (excluyendo caminos de una sola carretera)
- No dirigido: Contar personas en un mapa.
## 4. Representaciones
**Pregunta.** ¿Qué operación te parece más importante en un grafo: listar vecinos o preguntar si existe una arista? ¿Por qué? Listar vecinos porque es lo que genera interés, los nodos que no conectan no tienen relaciones útiles para el problema. Si enlisto todos los nodos guardo información inútil.
## 5. Interfaz común
**Pregunta.** ¿Por qué conviene que `GrafoListaAdyacencia` y `GrafoMatrizAdyacencia` tengan la misma interfaz? Porque ambas son implementaciones útiles para el mismo problema que convenimos usar en un caso u otro, pero las operaciones en general se conservam porque estamos usando la misma estructura de fondo, solo con una reprsentacion distinta.
## 6. Implementaciones
**Pregunta.** ¿Por qué un `set` ayuda a evitar aristas duplicadas? Porque el set elimina automáticamente repeticiones.
**Pregunta.** ¿Qué debe pasar con la matriz cuando agregas un vértice nuevo? Debería crear una nueva fila y en cada columna un False por defecto hasta que añadamos una arista nueva y entonces cambiamos el False. Ejemplo: Agregar arista entre 1 y 2 -> Cambia a True en la celda (1,2) y (2,1) porque no son dirigidos
## 7. Visualización con NetworkX
## 8. Diseño de pruebas
## 9. Patrón descubierto
## 10. Cierre