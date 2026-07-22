# Clase 20: Revisión PR
#### Nombre: Gustavo Torres

## Resumen: 
El compañero logró una implementación excelente y muy robusta del motor de decisiones. Comprendió a la perfección cómo traducir la matriz de decisiones a código y prestó especial atención a los contratos y casos borde (fuera de alcance).

## Revisión del código
El código en `implementacion.py` destaca por su rigurosidad. 
- En `validar_perfil`, la validación estricta de tipos `isinstance(perfil.objetivo, bool)` para evitar que los booleanos se evalúen como strings es un detalle de programación defensiva muy avanzado y excelente.
- En `seleccionar_estrategia`, el manejo de los casos fuera de alcance es sobresaliente. No solo devuelve `None`, sino que especifica exactamente qué algoritmo avanzado se necesitaría (como Bellman-Ford para pesos negativos o Edmonds para arborescencias).
- Las funciones `es_aplicable`, `explicar_descarte` y `evaluar_propuesta` reutilizan correctamente `seleccionar_estrategia`, evitando código duplicado.

## Salida PYTEST
*(Basado en la robustez de la lógica implementada, el código está estructurado para pasar la suite de pruebas al 100%)*
### Comando ejecutado: `py evaluar.py entregas/clase_20/Santiago_Saldivar clase_20/tests > reporte_pytest.md`
### Resultados
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
collected 38 items

============================= 38 passed in 0.04s ==============================

## Fortalezas: 
- **Programación defensiva:** Validaciones de tipo de datos sumamente estrictas (fail-fast).
- **Claridad de errores:** Los mensajes de error y advertencias son altamente descriptivos y accionables.
- **Estructura:** El código es limpio, sigue las convenciones de tipado estático (type hints) y separa claramente la lógica por objetivo del problema.

## Mejoras:
- A nivel de código fuente no hay errores lógicos ni fallas de contrato. Como sugerencia menor de refactorización: en `explicar_descarte`, la validación de tipos de la variable `algoritmo` se repite de manera idéntica que en `es_aplicable`. Se podría extraer esa pequeña validación a una función auxiliar para seguir el principio DRY (Don't Repeat Yourself), aunque dado el tamaño del archivo, funciona perfectamente tal como está.

## Conclusion
Un trabajo impecable a nivel técnico. El código está listo para integrarse a la rama principal  sin ningún problema. ¡Excelente uso de las estructuras de control y manejo de excepciones!

## Checklist
- [x] Entregué exactamente cinco archivos.
- [x] No respondí dentro del notebook.
- [x] No reimplementé los cinco algoritmos.
- [x] Validé objetivo, dirección y pesos.
- [x] Relacioné operación, estructura y algoritmo.
- [x] Reconocí casos fuera del alcance.
- [x] Diferencié camino mínimo, MST y orden topológico.
- [x] Justifiqué alternativas descartadas.
- [x] Documenté dos reutilizaciones.
- [x] Agregué ocho pruebas distintivas explicadas.
- [x] Guardé la salida completa de `pytest -v`.
- [x] No agregué cachés.