Discusión técnica — Clase 20

Nombre:
Escenario 1

    Problema y objetivo: conectar calles
    Dirección y pesos: no dirigidas, peso 0 o 1
    Operación dominante: elegir aristas y sumar peso
    Estructura y algoritmo: heap, BFS 0 1
    Contrato: pesos 0 o 1,
    Alternativa descartada:BFS
    Módulo previo reutilizado:BFS 0 1
    Adaptación de entrada/salida: Los nodos son las calles
    Prueba distintiva:Probar que encuentre la ruta mínima
    Complejidad e interpretación: O(V+E)

Escenario 2

    Problema y objetivo: Conectar y renovar todos los edificios
    Dirección y pesos: Renovaciones dirigidas, conexiones no dirigidas
    Operación dominante: Encontar menor ruta, cumplir requisitos
    Estructura y algoritmo: Kruskal, Kahn
    Contrato: sin pesos negativos
    Alternativa descartada: BFS
    Módulo previo reutilizado: Kruskal, Kahn
    Adaptación de entrada/salida: Los nodos ahora son edificios en Kruskal, en Khan ahora son prerrequisitos técnicos
    Prueba distintiva: Probar que encuentre las rutas
    Complejidad e interpretación: log e, O(v+e)

Caso fuera del alcance
Casos con aristas negativas
Reflexión final
La elección del algoritmo depende mucho del contexto de cada problema.