# Respuestas del Cuaderno de Trabajo - Clase 18 - Gustavo Torres

**Pregunta inicial:** ¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?
**Respuesta:** Ordenando todas las conexiones posibles de la más barata a la más cara, y aceptándolas una por una siempre y cuando no cierren un círculo (ciclo) con las que ya elegimos. Para esto usamos Kruskal apoyado en la estructura Union-Find.

---

**Sección 1:** ¿Qué producto final esperamos obtener hoy y en qué se diferencia de un camino desde un origen?
**Respuesta:** Esperamos obtener un "árbol de expansión mínima", que es básicamente el esqueleto más barato que conecta todos los puntos. A diferencia de Dijkstra, aquí no hay un punto de inicio y no nos importa la distancia de un nodo A a un nodo B, solo nos importa conectar toda la red al menor costo global.

**Sección 2:** ¿Qué operación dominante distingue a Kruskal de BFS, 0-1 BFS y Dijkstra?
**Respuesta:** Kruskal se la pasa haciendo una sola pregunta clave: "¿Estos dos puntos ya están en el mismo grupo?". En lugar de sumar distancias, su trabajo principal es verificar conectividad para no hacer ciclos.

**Sección 3:** ¿Por qué no basta aceptar automáticamente todas las carreteras en orden creciente de costo?
**Respuesta:** Porque a veces la carretera más barata conecta dos ciudades que, dando una vuelta por otras rutas que ya aceptaste, ¡ya estaban conectadas! Estarías cerrando un ciclo y desperdiciando costo en una ruta redundante.

**Sección 4:** ¿Qué optimiza cada algoritmo y cuál de ellos necesita un origen?
**Respuesta:** Dijkstra optimiza la distancia desde un punto de inicio hacia los demás (necesita un origen a fuerzas). Kruskal optimiza el costo total de toda la infraestructura junta (no tiene ni necesita origen).

**Sección 5:** ¿Por qué un árbol de expansión conectado con V vértices tiene exactamente V−1 aristas?
**Respuesta:** Imagina los vértices sueltos. Cada línea que agregas fusiona dos grupos en uno. Para que todos queden en un solo grupo unificado, necesitas dar exactamente V-1 "pegamentos" (aristas). Si pones una más, a fuerzas cierras un ciclo.

**Sección 6:** ¿Qué información mínima necesitamos antes de aceptar una arista u–v?
**Respuesta:** Solo necesitamos saber si "u" y "v" ya pertenecen al mismo equipo/componente. Si ya están, la rechazamos; si están en equipos distintos, la aceptamos y los unimos.

**Sección 7:** ¿Qué cambia en la partición cuando aceptamos una arista entre componentes distintas?
**Respuesta:** Los dos grupos separados se fusionan en un solo mega-grupo. Al hacer esto, el conteo total de componentes independientes disminuye en 1.

**Sección 8:** ¿Por qué conviene que union(a, b) devuelva un booleano?
**Respuesta:** Porque mata dos pájaros de un tiro: ejecuta la unión internamente y nos avisa al instante si valió la pena (`True`) o si la rechazó porque cerraba un ciclo (`False`).

**Sección 9:** ¿Qué condición permite reconocer una raíz en el arreglo padre?
**Respuesta:** Que el nodo apunte a sí mismo. Es decir, que el valor guardado en esa posición del arreglo sea igual a su propio índice (`padre[i] == i`).

**Sección 10:** ¿Por qué debemos validar explícitamente los índices negativos?
**Respuesta:** Porque Python es mañoso y si le pides el índice `-1` te va a dar el último elemento de la lista sin marcar error. Esto arruinaría la matemática de la estructura, necesitamos que truene explícitamente con un `IndexError`.

**Sección 11:** ¿Qué error aparece si union enlaza nodos arbitrarios sin encontrar primero sus raíces?
**Respuesta:** Destrozas la estructura del árbol. Dejarías pedazos del grupo desconectados de la raíz principal, rompiendo componentes que supuestamente ya estaban unidas y causando falsos ciclos.

**Sección 12:** ¿Qué invariantes viola padre = [1, 0, 2]?
**Respuesta:** Viola la regla de que "no existen ciclos" y de que "toda cadena termina en una raíz". Aquí el 0 apunta al 1, y el 1 apunta al 0, creando un ciclo infinito donde `find` se quedaría atorado para siempre.

**Sección 13:** ¿Qué cambia y qué permanece igual durante la compresión de caminos?
**Respuesta:** Cambia la forma interna del árbol (se aplasta y se vuelve más directo porque los nodos ahora apuntan directo al jefe máximo). Lo que se mantiene exactamente igual es quién pertenece a qué grupo y el número total de componentes.

**Sección 14:** ¿Por qué colocar el árbol pequeño debajo del grande limita el crecimiento de altura?
**Respuesta:** Porque si cuelgas el grupo chiquito bajo el grande, solo estás agregando un pasito extra para llegar a la raíz a unos pocos nodos. Si lo hicieras al revés, afectarías a la mayoría, haciendo los caminos mucho más largos inútilmente.

**Sección 15:** ¿Qué devuelve union(0, 3) después de unir las componentes {0,1} y {2,3}?
**Respuesta:** Devuelve `True`, porque el grupo del 0 y el grupo del 3 todavía son independientes en ese momento. Al unirlos, el contador total baja a 3 componentes.

**Sección 16:** ¿Cómo usa Kruskal el booleano devuelto por union?
**Respuesta:** Lo usa como filtro. Si `union` dice `True`, Kruskal dice "perfecto, la cobro y la agrego al esqueleto". Si da `False`, dice "paso, es un ciclo" y se la salta.

**Sección 17:** ¿Cuál es el costo final del ejemplo conductor y por qué se detiene después de cuatro aristas?
**Respuesta:** El costo final es 8. Se detiene rápido porque son 5 ciudades, y sabemos matemáticamente que con V-1 (es decir, 4 aristas) ya tienes todo conectado. Seguir revisando sería perder el tiempo.

**Sección 18:** ¿Qué condición permite distinguir un MST completo de un bosque desconectado?
**Respuesta:** Checar si logramos recolectar exactamente V-1 aristas al final del ciclo. Si recolectamos menos, significa que nos quedamos sin opciones antes de terminar y el grafo tiene zonas aisladas (está desconectado).

**Sección 19:** ¿Por qué un test con pesos empatados no debe exigir siempre una lista exacta de aristas?
**Respuesta:** Porque si dos conexiones cuestan lo mismo, el algoritmo puede agarrar cualquiera de las dos primero y el costo final será igual de bueno. Hay más de un árbol correcto, así que la prueba solo debe validar el costo y que conecte todo, no el orden exacto.

**Sección 20:** ¿Qué parte domina la complejidad total de Kruskal?
**Respuesta:** Ordenar la lista de aristas de la más barata a la más cara al inicio. Eso toma $O(E \log E)$ y es el cuello de botella del algoritmo.

**Sección 21:** ¿Qué dos adaptaciones separan el formato de CSES de nuestra función reutilizable?
**Respuesta:** 1) CSES cuenta las ciudades del 1 al N, mientras que nosotros usamos índices del 0 al N-1 (hay que ajustar al leer). 2) Si el grafo está desconectado, CSES exige imprimir el texto "IMPOSSIBLE" en lugar de que devolvamos `None`.

**Sección 22:** ¿Qué cambia entre Redundant Connection y Kruskal aunque ambos usen Union-Find?
**Respuesta:** Que en Redundant Connection las aristas no se ordenan por costo. Solo las vas procesando en el orden que te las dan hasta que `union` te escupa `False`, esa es la arista que sobra.

**Sección 23:** ¿Qué responsabilidades deben estar probadas antes de integrar Union-Find dentro de Kruskal?
**Respuesta:** Tienes que estar seguro de que tu validación de índices funciona, que `find` devuelve la raíz y comprime bien, y que `union` une bien los tamaños y detecta los ciclos. Si el Union-Find tiene un bug, Kruskal va a fallar feo.

**Sección 24:** ¿Qué invariante protege una prueba de unión repetida?
**Respuesta:** Protege que si intentas unir dos cosas que ya están en el mismo grupo, el número total de componentes no debe bajar, ni las aristas o tamaños deben corromperse. Debe decir "no hice nada".

**Sección 25:** ¿Qué estructura se necesitaría para procesar tareas cuando unas dependen de otras?
**Respuesta:** Necesitas ver qué nodos no tienen dependencias pendientes e ir liberándolos. Eso se hace muy bien con un orden topológico manejado por una **cola** normalita.