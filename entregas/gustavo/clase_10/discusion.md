# Discusión - Clase 10: Recorridos de grafos

## 1. De representar a recorrer
En la clase pasada aprendí a dibujar el "mapa" de un problema, conectando cosas con nodos y aristas. Ahora di el siguiente paso: caminar por ese mapa. Recorrer un grafo no es más que moverme por esas conexiones de forma ordenada, con el cuidado de ir dejando "migajas de pan" (un registro de visitados) para no dar vueltas en círculos si el mapa tiene caminos cerrados.

## 2. Estrategias manuales
Hacer el recorrido a mano me ayudó a darme cuenta de que básicamente hay dos formas naturales de explorar un lugar desconocido. O reviso todo lo que tengo a un metro de distancia antes de alejarme más, o me voy por un solo pasillo hasta topar con pared y luego me regreso a buscar otras opciones. 

## 3. BFS (Búsqueda en Anchura)
Esta es la estrategia de ir nivel por nivel. Me la imagino como una mancha de agua extendiéndose. Para que funcione, me di cuenta de que necesito una **cola** (una fila normal). Al poner a los vecinos que voy encontrando al final de la fila, garantizo que primero voy a visitar a los que descubrí antes.

## 4. DFS (Búsqueda en Profundidad)
Esta es la estrategia de irme hasta el fondo. En lugar de una fila, aquí uso una **pila** (como una torre de platos). Cada que descubro vecinos nuevos, los pongo hasta arriba de la pila y siempre tomo el de hasta arriba. Esto me obliga a dejar en pausa caminos viejos y clavarme en lo más nuevo que acabo de encontrar.

## 5. Comparación
La principal diferencia está en la herramienta que usan y para qué sirven. 
* BFS usa una cola y es buenísimo si quiero encontrar el camino más corto (en cantidad de pasos) porque avanza de manera uniforme.
* DFS usa una pila y no me asegura el camino más rápido, pero es excelente y muy directo si solo quiero recorrer todo el terreno (como para contar cuántas zonas separadas hay).

## 6. Visualización
Ver el algoritmo en una animación es mil veces mejor que ver una lista de letras impresas en la consola. Al asignarle colores a los nodos (gris si no lo conozco, azul si está en la fila, rojo si lo estoy pisando y verde si ya terminé con él), pude entender perfectamente cómo la cola del BFS hace que los colores se expandan en círculos, mientras que la pila del DFS hace que el rojo viaje en zigzag por todo el mapa.

## 7. CSES
Pensar en los problemas de CSES me ayudó a aterrizar esto:
* En **Message Route**, donde importa mandar algo por la ruta más directa, BFS es el ganador.
* En **Counting Rooms**, donde solo me interesa iluminar toda una habitación para contarla, DFS hace el trabajo muy bien.
* En **Labyrinth**, BFS me ayudaría a encontrar la salida en la menor cantidad de pasos.

## 8. Pruebas
Hacer las pruebas me hizo pensar en los casos donde mi código se podría romper. Diseñé una prueba para un grafo con un solo nodo (para asegurarme de que no falle si no hay vecinos) y otra con un círculo cerrado para confirmar que mi conjunto de `visitados` sí me está protegiendo de entrar en un ciclo infinito.

## 9. Patrón descubierto
El patrón de recorrer grafos me parece como una receta universal: sin importar el problema, si tengo cosas conectadas, elijo un punto de partida, escojo mi herramienta (cola para ir a lo ancho o pila para ir profundo) y repito el proceso de visitar y anotar hasta que ya no quede nada pendiente.

## 10. Pregunta abierta
Me sigo preguntando cómo manejaríamos las cosas si los caminos tuvieran diferentes distancias. En estos ejercicios asumimos que de A a B hay la misma distancia que de B a C, pero si un pasillo mide 2 metros y el otro 50, siento que el BFS clásico ya no me daría la ruta más rápida. ¿Qué tendríamos que cambiar en la herramienta de la cola para solucionar esto?