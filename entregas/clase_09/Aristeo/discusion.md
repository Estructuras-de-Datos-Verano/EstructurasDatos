# Discusión

## 1. De secuencias a relaciones
Las secuencias ordenan elementos de forma lineal y son útiles cuando el problema es recorrer o procesar datos en un orden fijo. Las relaciones, en cambio, modelan cómo los elementos están conectados entre sí y permiten representar redes, rutas y dependencias que no siguen un solo eje.

## 2. Problemas CSES
Los problemas estudiados muestran cómo un mismo tipo de estructura puede tomar formas distintas: ciudades conectadas por carreteras, casillas libres vecinas en un tablero o celdas transitables en un laberinto. En todos los casos aparece una pregunta común, la de cómo explorar la red para descubrir componentes, caminos o la conectividad.

## 3. Elección de representación
La lista de adyacencia es preferible cuando hay pocos arcos en comparación con los vértices, porque guarda solo las conexiones existentes. La matriz de adyacencia se justifica cuando el grafo es muy denso o cuando se necesita responder inmediatamente si existe una arista entre dos vértices.

## 4. Polimorfismo
Tener una interfaz común para distintas representaciones permite escribir algoritmos que no dependen de la implementación interna. El polimorfismo hace posible alternar entre lista y matriz sin cambiar la lógica de recorrido o de búsqueda, y facilita comparar resultados con la misma API.

## 5. NetworkX
NetworkX es útil como herramienta de validación y visualización. Convertir un grafo propio a NetworkX permite aprovechar funciones maduras de dibujo y análisis, mientras se mantiene el control sobre la implementación pedagógica que se construyó desde cero.

## 6. Pruebas
Las pruebas deben concentrarse en el comportamiento público: agregar vértices, crear aristas, calcular el número de vértices y aristas, y evitar duplicados. No es necesario asumir detalles de la estructura interna; basta verificar que la salida y las propiedades públicas sean correctas.

## 7. Patrón descubierto
El patrón que aparece es el modelado de relaciones: identificar entidades y sus conexiones, estructurarlas como nodos y aristas, y elegir la representación más adecuada según la densidad y las operaciones necesarias.

## 8. Pregunta abierta
¿Cómo cambia la elección de representación cuando el grafo deja de ser estático y recibe adiciones y eliminaciones frecuentes de vértices y aristas?