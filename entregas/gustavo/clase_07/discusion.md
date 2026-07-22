# Discusión Técnica: Arquitectura y Diseño de Estructuras Monótonas

## 1. Problema y primera idea
El problema Nearest Smaller Values de CSES requiere encontrar, para cada posición de un arreglo, el índice más cercano a su izquierda cuyo valor sea estrictamente menor. 

Nuestra aproximación inicial e intuitiva consiste en emular una búsqueda exhaustiva lineal: al ubicarnos en un índice actual, retrocedemos iterativamente por las posiciones anteriores una por una hasta localizar el primer valor estrictamente menor o hasta agotar el prefijo, en cuyo caso asignamos 0. Aunque esta estrategia garantiza que la respuesta sea correcta al revisar todo por fuerza bruta, carece completamente de memoria algorítmica sobre las evaluaciones pasadas.

## 2. Por qué la solución ingenua repite trabajo
La ineficiencia del algoritmo ingenuo radica en que trata cada consulta como un proceso aislado. Al explorar hacia atrás, vuelve a examinar reiteradamente bloques de datos que ya habían sido evaluados por las posiciones anteriores. 

Si el arreglo presenta secuencias decrecientes largas, como montañas altas a la izquierda, cada nuevo elemento a la derecha se ve obligado a escalar y recorrer hacia atrás esas mismas estructuras una y otra vez. Este retrabajo redundante degrada el rendimiento del sistema, haciendo que el tiempo de ejecución en el peor de los casos crezca de forma proporcional al cuadrado del número de elementos.

## 3. Información útil e información descartable
El punto de inflexión para optimizar el problema proviene de formalizar el concepto de dominancia entre elementos. No todo el historial del prefijo es relevante para el futuro:

Información descartable o obsoleta: Si un elemento anterior es seguido por otro elemento más reciente cuyo valor es menor o igual, entonces el elemento más antiguo pierde toda utilidad para cualquier consulta futura. Al estar más alejado y tener un valor mayor o igual al elemento reciente, el número antiguo jamás podrá competir como la respuesta más cercana y estrictamente menor.

Información útil o candidatos viables: Son únicamente aquellos elementos que conforman una escalera inferior estrictamente creciente tanto en valor como en posición, es decir, los mínimos locales de cola. Todo valor que no pertenezca a esta escalera inferior puede ser borrado de la memoria sin alterar la correctitud del resultado.

## 4. Elección de estructura
Para gestionar este flujo dinámico donde necesitamos consultar el candidato válido más reciente y eliminar eficientemente por el extremo las evaluaciones obsoletas, la estructura de datos por excelencia es la pila monótona.

Su comportamiento de último en entrar, primero en salir encaja de manera natural con el principio de proximidad: el elemento en el tope representa el vecino izquierdo más cercano. Al retirar de la pila los elementos mayores o iguales antes de insertar el elemento actual, mantenemos limpia nuestra lista de candidatos útiles en tiempo real.

## 5. Variante: Nearest Greater Values
Al generalizar el problema para encontrar la posición del elemento estrictamente mayor más cercano a la izquierda, la estructura abstracta se conserva intacta, alterándose únicamente el criterio de purga.

En esta variante, un valor grande entrante vuelve obsoletos a los valores anteriores que sean menores o iguales. Por lo tanto, el bucle de limpieza invierte su condición: retiramos elementos de la pila mientras el tope sea menor o igual al valor actual. La estructura se transforma en una pila monótona estrictamente decreciente desde la base hasta el tope, preservando el mismo rendimiento lineal eficiente.

## 6. Contraejemplo: Maximum Subarray Sum
Es un error asumir que cualquier problema de optimización sobre subarreglos puede resolverse purgando historial con una pila monótona. En el problema de la suma máxima de subarreglo, la dominancia entre candidatos no depende de una posición única, sino que responde a una propiedad acumulativa continua.

Un número negativo intermedio reduce momentáneamente la suma, pero no vuelve inservible a su prefijo si los números positivos posteriores logran compensar la pérdida. Intentar descartar candidatos basándose exclusivamente en una monotonía local rompería la continuidad del intervalo. Por ello, este problema se resuelve mediante algoritmos de sumas acumuladas continuas como el algoritmo de Kadane, demostrando que la estructura elegida debe alinearse rigurosamente con la naturaleza del problema.

## 7. Sliding Window
Cuando nos enfrentamos a problemas sobre un intervalo móvil de tamaño fijo, como calcular la mediana o el mínimo en una ventana deslizante, la información adquiere un ciclo de vida acotado: los datos entran por la derecha, permanecen vigentes durante un número fijo de pasos, y obligatoriamente salen por la izquierda al expirar su tiempo.

Una pila monótona estándar resulta insuficiente aquí porque carece de la capacidad de expulsar elementos por la base de manera inmediata cuando expira la ventana. Para conservar la monotonía en este escenario, se requiere evolucionar a una cola doblemente terminada monótona, que permite limpiar elementos obsoletos por el final e invalidar elementos expirados por el frente al mismo tiempo y de forma constante.

## 8. Invariante
La solidez formal de nuestro algoritmo reposa en el mantenimiento estricto de una propiedad estructural invariable en cada ciclo de la ejecución:

Invariante: Al inicio y al término del procesamiento de cada elemento del arreglo, los pares de valor y posición contenidos dentro de la pila mantienen un orden estrictamente creciente tanto en la magnitud de sus valores como en sus posiciones, medidos desde el fondo hasta el tope.

Este invariante garantiza que el tope de la pila, tras el proceso de descarte, siempre corresponda de manera directa al resultado óptimo de la consulta actual.

## 9. Pruebas
El diseño de casos de prueba robustos debe enfocarse en poner a prueba los límites de nuestro algoritmo:

Verificación del operador estricto: Es obligatorio incluir pruebas con valores duplicados continuos y alternados. Si se comete el error de programar una comparación no estricta al limpiar la pila, la estructura no eliminará valores idénticos, arrojando falsos positivos en las consultas siguientes al romper el orden monótono.

Fronteras y casos degenerados: Evaluar arreglos de un solo elemento, secuencias estrictamente crecientes o decrecientes, y arreglos uniformes donde todos los elementos son iguales asegura que la estructura maneje los vaciados totales de la pila sin producir errores de ejecución.

## 10. Complejidad
A pesar de la presencia visual de un ciclo mientras anidado dentro de un ciclo para principal, la complejidad temporal del algoritmo es estrictamente lineal en relación al número de datos.

La demostración se sustenta en un análisis amortizado: cada uno de los elementos del arreglo ingresa a la pila exactamente una sola vez durante toda la ejecución del programa. Consecuentemente, un elemento solo puede ser retirado de la pila como máximo una vez. El número total de operaciones de entrada y salida en la estructura está acotado al doble del tamaño del arreglo, lo que arrojó un tiempo de ejecución lineal y un consumo de memoria auxiliar proporcional a la cantidad de elementos.

## 11. Cómo descubrimos el algoritmo
El hallazgo de la pila monótona no derivó de aplicar una receta algorítmica prefabricada, sino de un proceso sistemático de depuración del trabajo redundante:

Simulamos manualmente el problema identificando el cuello de botella, que era retroceder sobre los mismos elementos grandes una y otra vez.

Formulamos la regla lógica de dominancia que nos permitió deducir cuándo un dato pasado quedaba obsoleto por uno nuevo.

Al notar que requeríamos procesar siempre el candidato válido más reciente y eliminarlo por el mismo extremo si fallaba, la lógica de último en entrar, primero en salir nos condujo de forma orgánica a implementar una pila monótona.

## 12. Pregunta abierta
¿Cómo cambiaría la viabilidad conceptual y el tiempo de ejecución de la solución si el problema permitiera actualizaciones puntuales en tiempo real sobre el arreglo original, por ejemplo, modificar el valor de una posición cualquiera y posteriormente consultar de forma inmediata el valor menor más cercano para cualquier índice?

Reflexión: Una pila monótona estática perdería su utilidad, ya que una sola actualización en el pasado podría romper o alterar el orden monótono de todos los índices posteriores, forzándonos a explorar estructuras avanzadas de árboles de segmentos que permitan actualizar rangos de datos de manera dinámica.