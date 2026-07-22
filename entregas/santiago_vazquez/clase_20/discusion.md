# Escenario 1

## Problema y objetivo: Ir de recepción a laboratorio optimizando cantidad de pasillos; camino mínimo.  

## Dirección y pesos: Puede ser dirigido o no, sin pesos.  

## Operación dominante: Procesar vértices por capas.  

## Estructura y algoritmo: Cola y BFS.  

## Contrato: Cada arista aporta exactamente un paso.  

## Alternativa descartada: Dijkstra porque agrega un heap de manera innecesaria.  

## Módulo previo reutilizado: bfs_rutas de la Clase 16.

## Adaptación de entrada/salida: Convertir IDs de edificios a índices para matriz de adyacencia.

## Prueba distintiva: Un atajo con menos aristas pero ruta visualmente más larga.  

## Complejidad e interpretación: O(V+E); la lista devuelta es una ruta con el mínimo número de pasillos. 


# Escenario 2

## Problema y objetivo: Las calles tienen tiempos no negativos y se busca ruta al hospital; camino de costo mínimo.  

## Dirección y pesos: Grafo dirigido con pesos no negativos.  

## Operación dominante: Extraer la menor distancia tentativa.  

## Estructura y algoritmo: Heap y Dijkstra.  

## Contrato: No existen tiempos negativos.  

## Alternativa descartada: BFS porque minimiza número de aristas, ignorando el tiempo.  

## Módulo previo reutilizado: dijkstra_core de la Clase 18.

## Adaptación de entrada/salida: Parsear tiempos de aristas en tuplas (peso, destino).

## Prueba distintiva: Una ruta con más calles que debe ganar por menor tiempo total.  Complejidad e interpretación: O((V+E) log V); la distancia final es el menor tiempo conocido. 


# Caso fuera del alcance

Si usamos Dijkstra con pesos negativos, se rompe el contrato. La precondición exige valores positivos para garantizar que una distancia extraída del heap jamás mejorará. No invento soluciones absolutas ni parches mágicos porque la teoría indica explícitamente que los algoritmos abordados no cubren estos dominios.

# Reflexión final

Antes me dejaba llevar por la intuición y elegía estructuras según me sonaran lógicas. Ahora construyo modelos precisos extrayendo operaciones dominantes e identificando invariantes y restricciones del contrato. Aprendí que una herramienta solo es óptima si hace barata la operación que más requiere mi grafo.