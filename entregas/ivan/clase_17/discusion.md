# Discusión técnica — Clase 17

## 1. Nodo y lista ligada
El nodo es el contenedor individual que guarda un valor y la dirección de su vecino. La lista ligada es la estructura superior que administra a todos los nodos, controlando el tamaño y los accesos principales al inicio y al final.

## 2. Cola ligada
Necesita el frente para retirar elementos de inmediato y el final para enganchar los nuevos sin recorrer toda la estructura. Esto permite que tanto encolar como desencolar funcionen en tiempo constante O(1).

## 3. Invariantes
Cuando la cola está vacía, el frente debe ser None, el final debe ser None y el tamaño debe ser cero. Si alguna de estas tres condiciones no se cumple, la estructura está corrupta.

## 4. Lista simple y lista doble
La referencia anterior permite navegar en reversa y borrar desde el final en tiempo constante O(1). Su costo es que consume más memoria por cada nodo y duplica la obligación de actualizar los enlaces en cada inserción o remoción.

## 5. Deque
Una deque exige agregar y quitar elementos por ambos extremos en tiempo constante O(1). La lista doblemente ligada es adecuada porque el nodo final conoce a su antecesor, permitiendo su eliminación inmediata sin tener que escanear la lista de forma lineal.

## 6. Complejidad
Las listas nativas de Python son arreglos dinámicos en memoria contigua. Al usar pop(0), el primer elemento se borra y Python se ve obligado a desplazar físicamente todos los elementos restantes hacia la izquierda, lo que toma tiempo lineal O(n).

## 7. BFS
Deben marcarse al encolarse para evitar que un mismo nodo con múltiples vecinos comunes sea introducido varias veces a la cola de forma redundante. Omitir esto provoca un procesamiento duplicado o bucles infinitos en grafos cíclicos.

## 8. Predecesores
Su responsabilidad es registrar de qué nodo provino el descubrimiento de cada vértice. Funciona como un mapa comprimido que permite reconstruir la ruta óptima de reversa hasta el origen sin gastar memoria guardando caminos completos durante el viaje.

## 9. Reutilización
Porque a la función reconstructora no le importa qué algoritmo calculó las prioridades. Ambos métodos devuelven la misma topología de salida: un diccionario de paternidad que simplemente se camina de reversa desde el destino hasta el origen.

## 10. 0-1 BFS
Se agregan al inicio porque representan atajos gratuitos que no aumentan la distancia acumulada. Para mantener la cola ordenada por capas de costo mínimo sin usar un heap, estos nodos deben procesarse inmediatamente pasándole por delante a los de costo 1.

## 11. Comparación
BFS clásico usa una cola FIFO común para grafos sin pesos o con pesos idénticos. 0-1 BFS utiliza una deque para procesar pesos binarios de cero y uno. Dijkstra emplea un heap para resolver el caso general de pesos no negativos cualesquiera.

## 12. Elección de estructura
El procesamiento por capas en orden estricto de llegada conduce a una cola. La necesidad de separar el flujo en dos prioridades absolutas (costo cero o uno) conduce a una deque. Extraer siempre el mínimo global dinámico conduce a un heap.
## 13. Producción
Usaríamos la herramienta nativa de Python porque ya está optimizada para ser muy rápida. En código real es mejor usar algo que ya maneja la memoria eficientemente en lugar de construir nuestros propios nodos manuales desde cero.

## 14. Riesgos
Dejar punteros residuales o fantasmas al no borrar bien los nodos borrados. También es peligroso olvidar actualizar ambas direcciones; como la lista es doble, si cambias el sucesor pero olvidas el antecesor, la estructura pierde consistencia y se rompe.

## 15. Cierre
Elegiría un heap y el algoritmo de Dijkstra. 0-1 BFS ya no sirve porque la deque solo tiene dos extremos (inicio y final) para ordenar pesos de 0 y 1. Si agregamos un peso 2, no hay un lugar en medio para guardarlo sin desordenar todo.