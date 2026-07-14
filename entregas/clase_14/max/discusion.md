# Discusión_calse_14_Max

## Operación dominante.

La operación clave aquí no es buscar un valor en medio del grupo, sino obtener y sacar rápido los dos pesos más grandes. Un max-heap es perfecto para esto porque mantiene el mayor elemento siempre arriba, permitiendo sacarlo y meter la diferencia de inmediato.

## FIFO vs prioridad.

A diferencia de una cola FIFO donde el primero en llegar es el primero en salir (como una fila del banco), una cola de prioridad decide el orden según la importancia o el valor del elemento. En nuestro caso, salen primero las piedras más pesadas sin importar cuándo llegaron.

## BST/AVL vs heap.

Los árboles binarios de búsqueda (BST/AVL) mantienen todo perfectamente ordenado de izquierda a derecha, lo que cuesta más esfuerzo mantener. Un heap es más relajado: solo le importa que el jefe esté arriba de sus hijos, siendo más rápido para crear y usar si solo buscas extremos.

## Propiedad min-heap.

Es la regla de oro que obliga a que cualquier nodo sea menor o igual que sus nodos hijos. Gracias a esto, te aseguras de manera natural que el valor más pequeño de toda la estructura se quede siempre flotando en la raíz, listo para ser consultado.

## Representación por arreglo.

Aunque visualmente pensamos en un árbol, internamente usamos una lista simple de Python para ahorrar memoria y punteros. Los hijos y padres se calculan con fórmulas matemáticas exactas sobre los índices, logrando un acceso directo y súper veloz a cualquier posición.

## Sift-up.

Es el proceso de "subir" un elemento recién insertado al final del arreglo. Si el nuevo valor es más chico que su padre, se van intercambiando posiciones repetidamente hacia arriba hasta que encuentra su lugar correcto y no rompe la regla del min-heap.

## Sift-down.

Se usa al extraer el mínimo: ponemos la última piedra en la raíz y la hacemos "bajar" comparándola con sus hijos. Se intercambia con el menor de ellos de nivel en nivel hasta que queda bien acomodada, restaurando el orden del árbol.

## Complejidad.

Construir el heap desde cero toma un tiempo eficiente de complejidad constante. Por otro lado, cada turno del juego realiza operaciones de extracción e inserción que complejidad logaritmica, lo que nos da un tiempo total impecable de complejidad logaritmica en lugar de tardar demasiado.

## Last Stone Weight.

Es el juego donde hacemos chocar las dos piedras más pesadas de un multiconjunto hasta que quede una o ninguna. Si tienen el mismo peso se destruyen, y si son diferentes, la diferencia se vuelve a meter al heap para seguir jugando.

## Pruebas propias.

Diseñamos tres escenarios clave en los tests estudiantiles para asegurar el código: test_max1 para una inserción con varias subidas, test_max2 para una extracción que baja múltiples niveles, y test_max3 como caso extremo de piedras grandes con duplicados que se anulan.

## Revisión técnica.

Corregimos errores críticos de sintaxis en el código original, como la falta de paréntesis al llamar a esta_vacio(), el error al medir el tamaño de la clase en vez de la lista, y aseguramos que se lance IndexError para que coincida con tus pruebas.

## Relación con Dijkstra.

El algoritmo de Dijkstra usa este mismo concepto para calcular rutas cortas: necesita extraer repetidamente el nodo con la menor distancia acumulada. Al usar un min-heap como el tuyo, esa selección se vuelve increíblemente rápida en lugar de revisar todo el mapa.

## Pregunta abierta: ¿qué operación haría preferible otra estructura?

Las operaciones de tipo FIFO no necesitan de este tipo de estructuras, de echo todo lo contrario.
