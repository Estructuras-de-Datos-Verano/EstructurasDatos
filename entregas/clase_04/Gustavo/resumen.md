***Reflexión***

Implementación más clara: La`PilaLista`fue la más clara y natural para empezar, debido a que aprovecha directamente los métodos nativos de las listas de Python de forma muy directa.

Implementación más eficiente: La`PilaDeque`parece ser la más eficiente para realizar muchas operaciones porque utiliza collections.deque, una herramienta diseñada específicamente para optimizar el rendimiento en los extremos de la estructura

Aprendizaje sobre`pytest`:Aprendí que`pytest`facilita la organización de pruebas automáticas mediante convenciones de nombres como la carpeta`tests/`y prefijos`test_`.

Prueba más importante: La prueba parametrizada que verifica que el método`pop()`respete estrictamente el principio LIFO

Duda pendiente: Me queda la duda exacta de cómo cambian las referencias de la cima y los nodos en los métodos`push`y`pop`dentro de la implementación PilaNodo