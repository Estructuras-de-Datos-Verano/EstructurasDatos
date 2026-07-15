# NOtebook Aristeo

| Contrato | Entrada mínima | Observado | Esperado | Test propuesto |
| --- | --- | --- | --- | --- |
| peso no negativo | | | | |
| vecino implícito | | | | |
| origen válido | | | | |
| entrada obsoleta | | | | |
| representación | | | | |
## 1. De algoritmo correcto a software confiable
### ¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable?
...
## 2. Un orden profesional de lectura
### ¿Por qué conviene leer firma y docstring antes que el while principal?
...
## 3. Tipos como decisiones de diseño
### ¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list?
...
## 4. Normalización y copia defensiva
### ¿Qué dos problemas resuelve _normalizar_grafo antes de ejecutar Dijkstra?
...
## 5. TypeError y ValueError cuentan historias distintas
### ¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación?
...
## 6. Bool, NaN e infinito
### ¿Por qué True y NaN requieren comprobaciones específicas?
...
## 7. Vecinos implícitos y representación total
### ¿Qué fallo evita resultado.setdefault(vecino, [])?
...
## 8. El contrato de dijkstra
### ¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino?
...
## 9. Estado inicial y tablas totales
### ¿Qué invariante establecen las comprensiones antes del while?
...
## 10. El guard clause de entradas obsoletas
### ¿Qué garantiza la comparación inmediatamente posterior a heappop?
...
## 11. Relajación y actualización atómica
### ¿Qué datos deben actualizarse juntos cuando una candidata mejora?
...
## 12. Reconstruir es otro problema
### ¿Qué diferencia hay entre destino inalcanzable y destino ausente?
...
## 13. Coordinación sin duplicación
### ¿Qué responsabilidades delega camino_minimo?
...
## 14. Del contrato a una matriz de pruebas
### ¿Qué dimensión del contrato no se verifica al probar únicamente el costo final?
...
## 15. Auditoría de una implementación frágil
### ¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar?
...
## 16. Clínica de depuración
### ¿Qué información mínima debe contener un reporte de fallo útil?
...
## 17. Revisión profesional de código
### ¿Qué hace que un comentario de revisión sea accionable y verificable?
...
## 18. Complejidad sin perder robustez
### ¿La normalización cambia la complejidad asintótica de Dijkstra?
...
## 19. Cuatro algoritmos, cuatro operaciones dominantes
### ¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre?
...
## 20. Cierre
### ¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad?