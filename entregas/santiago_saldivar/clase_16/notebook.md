# Notebook

### Santiago Saldivar

## 1. De algoritmo correcto a software confiable
**Pregunta:** ¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable?
Que funcione con entradas distintas a las que esperábamos inicialmente.

## 2. Un orden profesional de lectura
**Pregunta:** ¿Por qué conviene leer firma y docstring antes que el while principal?
Porque explica de qué trata el código y qué hace antes de entrar a lo más técnico.

## 3. Tipos como decisiones de diseño
**Pregunta:** ¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list?
El objeto no es necesariamente un diccionario. Sequence admite listas y tuplas.

## 4. Normalización y copia defensiva
**Pregunta:** ¿Qué dos problemas resuelve _normalizar_grafo antes de ejecutar Dijkstra?
Valida que cada nodo y arista funcione bien, y que cada número que tiene cumpla las condiciones necesarias para tener una representación interna uniforme.

## 5. TypeError y ValueError cuentan historias distintas
**Pregunta:** ¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación?
TypeError salta si los objetos no son los que necesitamos. Value si sí son del tipo necesario, int o str, por ejemplo, pero no tienen el valor necesario, por ejemplo, ser negativos.

## 6. Bool, NaN e infinito
**Pregunta:** ¿Por qué True y NaN requieren comprobaciones específicas?
Porque son objetos que funcionan distinto.

## 7. Vecinos implícitos y representación total
**Pregunta:** ¿Qué fallo evita resultado.setdefault(vecino, [])?
KeyError

## 8. El contrato de dijkstra
**Pregunta:** ¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino?
Porque encuentra las rutas entre los nodos en general. Cada nodo es clave para sus adyacencias. La función que compara es otra.

## 9. Estado inicial y tablas totales
**Pregunta:** ¿Qué invariante establecen las comprensiones antes del while?
Cada clave interna existe en ambos mapas.

## 10. El guard clause de entradas obsoletas
**Pregunta:** ¿Qué garantiza la comparación inmediatamente posterior a heappop?
Que sólo si la candidatura coincide con el valor vigente recorremos las aristas

## 11. Relajación y actualización atómica
**Pregunta:** ¿Qué datos deben actualizarse juntos cuando una candidata mejora?
El predecesor y el peso

## 12. Reconstruir es otro problema
**Pregunta:** ¿Qué diferencia hay entre destino inalcanzable y destino ausente?
El destino inalcanzable está en el grafo pero no conecta con nada. EL ausente no es parte del grafo.

## 13. Coordinación sin duplicación
**Pregunta:** ¿Qué responsabilidades delega camino_minimo?
La construcción de Dijkstra

## 14. Del contrato a una matriz de pruebas
**Pregunta:** ¿Qué dimensión del contrato no se verifica al probar únicamente el costo final?
Los tipos.

## 15. Auditoría de una implementación frágil
**Pregunta:** ¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar?

### No valida el grafo
1. contrato incumplido;

No se asegura de recibir objetos en forma necesaria.

2. entrada mínima reproducible;

grafo = {"A": [("B", 1), ("D", 3)], "B":[("D", 1)]}
    costo, camino = camino_minimo(grafo, "A", "")

3. resultado observado;

Error

4. resultado esperado;

Encontrar ruta mínima

5. prueba automatizada;

pytest

6. cambio localizado.

Agregar validación

### Acepta pesos negativos
1. contrato incumplido;

Sólo debe aceptar positivos

2. entrada mínima reproducible;

grafo = {"A": [("B", -1), ("D", 3)], "B":[("D", 1)], "D": [] }
    costo, camino = camino_minimo(grafo, "A", "D")

3. resultado observado;

Bajó en un momento.

4. resultado esperado;

Ruta mínima que sólo aumente.

5. prueba automatizada;

pytest

6. cambio localizado.

Validación

### No incluye vecinos implícitos
1. contrato incumplido;

Debe incluir vecinos implícitos

2. entrada mínima reproducible;

grafo = {"A": [("B", 1), ("D", 3)], "D": [] }
    costo, camino = camino_minimo(grafo, "A", "D")

3. resultado observado;

Error

4. resultado esperado;

Toma en cuenta el vecino implícito, aunque no esté explícito en el grafo.

5. prueba automatizada;

pytest

6. cambio localizado.

Agregar todos los nodos a un diccionario interno en la función

## 16. Clínica de depuración
**Pregunta:** ¿Qué información mínima debe contener un reporte de fallo útil?
Dónde y por qué, exactamente, se da el error.

## 17. Revisión profesional de código
**Pregunta:** ¿Qué hace que un comentario de revisión sea accionable y verificable?
Que sea útil para corregir y se pueda reproducir lo que hizo el comentor.

## 18. Complejidad sin perder robustez
**Pregunta:** ¿La normalización cambia la complejidad asintótica de Dijkstra?
No. La fase lineal no domina al término logarítmico general.

## 19. Cuatro algoritmos, cuatro operaciones dominantes
**Pregunta:** ¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre?
FIFO, min-heap, ordenamiento + conjuntos disjuntos, grados + cola

## 20. Cierre
**Pregunta:** ¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad?
Epezar con firmas y docstrings, luego pasar al código.
