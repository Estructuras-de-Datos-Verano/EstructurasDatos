# Clase 16: Discusión
#### Nombre: Patricio Navarro

## 1. Diferencia entre algoritmo correcto y función robusta.
- Algoritmo correcto: funciona para un caso específico de prueba y sigue una idea correcta pero para casos en general puede fallar.
- Función robusta: maneja todo tipo de errores, como Typeerrors y ValueErrors, es mucho más a prueba de un mal uso o entradas que no se pueden usar.
## 2. Razón de separar normalización.
- Poder manejar una copia defensiva.
- Reducir número de condiciones.
## 3. Mapping/Sequence frente a dict/list.
- Mapping/Sequence permiten varios tipos de objetos mientras cumplan con la característica necesaria.
- dict/list son objetos más específicos.
## 4. TypeError frente a ValueError.
- TypeError: cuando se usa un tipo de dato que no debería de poder usarse.
- ValueError: cuando la entrada se sale del dominio de la función.
## 5. Bool, NaN e infinito.
- Bool: instancia de `int`, por lo que un True puede pasar.
- NaN: instancia de `float`, también puede pasar y arruina condicionales.
- infinito: manejar cuando es inalcanzable o ausente.
## 6. Copia defensiva.
- Forma de evitar que se manejen datos de la entrada y se altere en el proceso.
## 7. Vecino implícito.
- Nodo fantasma, que tiene vecinos que llegan a él pero él no llega a nadie.
## 8. Invariante de entradas obsoletas.
- Eliminarlas pues son mayores que una relajación.
## 9. Responsabilidades de reconstrucción.
- Apoyarse de camino_minimo para marcar los predecesores y reconstruir el camino que se siguió.
## 10. Matriz contrato–riesgo–prueba.
- Buena forma de depurar posibles errores y entender el comportamiento esperado.
## 11. Complejidad de normalización y Dijkstra.
- O((V+E)log(V)), es la misma complejidad porque lo que tarda un poco más se absorbe en otras acciones.
## 12. Operación dominante en BFS, Dijkstra, Kruskal y topológico.
- BFS: menor número de aristas.
- Dijkstra: menor suma no negativa.
- Kruskal: árbol expandido.
- Topológico: representar dependencias.
