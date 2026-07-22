# Discusión técnica
# Nombre: José Iván Reyna Blanco
## Escenario 1

- Problema y objetivo: Conectar todos los edificios de la universidad gastando lo menos posible en el total del cableado.
- Dirección y pesos: Conexiones de doble sentido donde el costo (siempre positivo) es el precio de instalar cada enlace.
- Operación dominante: Buscar continuamente las partes que aún no están conectadas y unirlas usando la opción más barata disponible.
- Estructura y algoritmo: Usamos un agrupador rápido (Union-Find) y el método para armar redes baratas (Kruskal).
- Contrato: Entregar las conexiones exactas para unir todo sin hacer círculos inútiles, y avisar si algún edificio queda completamente aislado.
- Alternativa descartada: Buscar el camino más corto desde un solo punto (Dijkstra) crearía rutas individuales buenas, pero elevaría muchísimo el costo global del proyecto.
- Módulo previo reutilizado: Se reutiliza el código anterior de Kruskal (`entregas.clase_18.Pato.kruskal`).
- Adaptación de entrada/salida: Le pasamos al código las opciones ordenadas de la más barata a la más cara, y nos devuelve qué cables instalar.
- Prueba distintiva: Si hay tres edificios, este método los conecta en cadena por fuera (más barato) en lugar de mandar cables individuales desde el centro (más caro).
- Complejidad e interpretación: El cálculo es rápido y el resultado te da el plano exacto para conectar todo el campus al menor costo posible.

## Escenario 2

- Problema y objetivo: Encontrar la ruta de calles que le tome menos tiempo a una ambulancia para llegar a un accidente.
- Dirección y pesos: Calles con un sentido definido donde el costo (siempre positivo) representa los minutos que tardas en cruzarlas.
- Operación dominante: Revisar constantemente las opciones y elegir siempre el siguiente paso que tome menos tiempo acumulado desde el inicio.
- Estructura y algoritmo: Usamos un organizador de prioridades (Heap) y el método para buscar rutas óptimas (Dijkstra).
- Contrato: Entregar las instrucciones paso a paso para llegar lo antes posible, o avisar si el destino está bloqueado y es inalcanzable.
- Alternativa descartada: El método de contar calles (BFS) elegiría avenidas directas atascadas de tráfico; ignoraría que dar vuelta por más calles despejadas es más rápido.
- Módulo previo reutilizado: Se reutiliza el código anterior de búsqueda de rutas (`entregas.clase_16.Pato.dijkstra`).
- Adaptación de entrada/salida: Le pasamos el mapa de la ciudad como un diccionario, y el código nos devuelve la ruta ordenada lista para leerse como GPS.
- Prueba distintiva: Si una avenida directa toma 15 minutos, pero dar la vuelta por dos calles cortas toma 8 minutos, este método elegirá inteligentemente la ruta de 8 minutos.
- Complejidad e interpretación: Funciona de forma muy eficiente y te da la lista exacta de calles que debes seguir para evadir el tráfico y llegar pronto.

## Caso fuera del alcance

1. Estos métodos fallan si avanzar en una ruta te "devuelve tiempo o dinero" (costos negativos). Asumen que cada paso cuesta algo, y si hay valores negativos se atrapan en ciclos infinitos y fallan.
2. No debes forzar una solución inventada que ignore las reglas del problema, ya que solo estarías escondiendo errores graves de lógica que explotarán después.

## Reflexión final

Al inicio del curso, elegía mis herramientas adivinando o dejándome llevar por cómo sonaban las palabras, sin entender qué pasaba por debajo.
Ahora, me hago las preguntas correctas y pongo todo en ejemplos manuales para entender cómo se comporta el problema y elegir la herramienta perfecta con fundamentos. Me hubiera encantado tener más tiempo para hacer las prácticas en las que me atrasé y poder así comprender mejor sin apoyarme de IA; la tuve que usar inevitablemente para hacer debugs, crear buenas pruebas y llenar los docstrings adecuadamente. Creo que algo importante en el aprendizaje es poder hacer todo esto sin ayuda de la IA. 