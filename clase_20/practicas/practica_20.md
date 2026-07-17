# Práctica 20 — Laboratorio integrador de decisiones

## Idea central

Esta práctica no pide programar cinco algoritmos. Pide demostrar que puedes **modelar**, **elegir**, **rechazar**, **reutilizar**, **probar** y **explicar**.

Trabaja únicamente en `entregas/clase_20/nombre/`.

## Entrega exacta

```text
entregas/clase_20/nombre/
├── implementacion.py
├── test_estudiante.py
├── notebook.md
├── discusion.md
└── reporte_pytest.md
```

Copia `clase_20/src/seleccion_estrategias_base.py` como `implementacion.py`. Conserva firmas, dataclasses, excepciones y vocabulario.

## Parte 1 — Validar perfiles

Implementa `validar_perfil`.

- solo acepta `PerfilProblema`;
- `objetivo` y `tipo_pesos` son cadenas;
- `dirigido` es exactamente `bool`;
- objetivos: `camino_minimo`, `conexion_minima`, `orden_dependencias`;
- pesos: `sin_pesos`, `cero_uno`, `no_negativos`, `incluye_negativos`;
- tipos incorrectos lanzan `TypeError`; valores desconocidos, `ValueError`.

## Parte 2 — Seleccionar estrategia

Implementa `seleccionar_estrategia` conforme a la matriz del notebook. Devuelve siempre `DecisionAlgoritmica`.

- BFS + cola para camino sin pesos;
- 0-1 BFS + deque para pesos 0/1;
- Dijkstra + heap para pesos no negativos;
- Kruskal + Union-Find para conexión mínima no dirigida con costos;
- Kahn + cola/grados para dependencias dirigidas sin pesos;
- `algoritmo=None`, `estructura=None` y advertencia explicativa cuando ningún algoritmo estudiado aplica.

No introduzcas Bellman-Ford, Prim u otro algoritmo nuevo.

## Parte 3 — Aplicabilidad y descartes

Implementa `es_aplicable` y `explicar_descarte`. La explicación debe nombrar el límite del candidato y, cuando exista, la recomendación. Compartir una estructura no basta: BFS y Kahn usan cola con invariantes diferentes.

## Parte 4 — Evaluar propuestas

`evaluar_propuesta` devuelve `(valida, errores)`.

- valida tipos y algoritmo conocido;
- detecta por separado algoritmo y estructura incorrectos;
- ante un perfil fuera del alcance, nunca acepta una propuesta conocida;
- los mensajes deben ser accionables.

## Parte 5 — Reutilización documentada

En `discusion.md`, elige dos escenarios del notebook y describe cómo llamarías a la implementación de una clase anterior. Incluye:

1. módulo reutilizado;
2. adaptación de entrada;
3. precondición validada;
4. significado del retorno;
5. caso de prueba distintivo.

No copies el cuerpo del algoritmo.

## Parte 6 — Pruebas propias

Escribe al menos ocho pruebas explicadas:

1. BFS vs Dijkstra;
2. 0-1 BFS vs BFS;
3. Dijkstra vs Kruskal;
4. BFS vs Kahn;
5. pesos negativos fuera del alcance;
6. Kruskal con peso negativo;
7. error solo de estructura;
8. perfil inválido.

Para cada una registra regla, entrada, resultado esperado, alternativa descartada y relevancia.

## Parte 7 — Presentación del equipo

En tres minutos presenta: problema, objetivo, restricciones, operación dominante, estructura, algoritmo, contrato, prueba distintiva, complejidad e interpretación. Todo integrante debe poder responder qué cambiaría con otra dirección o dominio de pesos.

## Comandos

```bash
python3 evaluar.py entregas/clase_20/nombre clase_20/tests
python3 evaluar.py entregas/clase_20/nombre clase_20/tests entregas/clase_20/nombre/test_estudiante.py
```

## GitHub

Rama: `clase-20-nombre`.

PR: `[Clase 20] Nombre - Laboratorio integrador`.

Commits sugeridos:

```text
[FEAT] Modela perfiles y valida contratos
[FEAT] Selecciona estrategias por operación dominante
[TEST] Distingue caminos, MST y dependencias
[DOC] Justifica descartes y reutilización
[DOC] Cierra reflexión del curso
```

Antes del PR ejecuta `git branch --show-current`, `git status` y `git diff --name-only origin/main`. Solo deben aparecer los cinco archivos de tu entrega.

## Checklist

- [ ] Entregué exactamente cinco archivos.
- [ ] No respondí dentro del notebook.
- [ ] No reimplementé los cinco algoritmos.
- [ ] Validé objetivo, dirección y pesos.
- [ ] Relacioné operación, estructura y algoritmo.
- [ ] Reconocí casos fuera del alcance.
- [ ] Diferencié camino mínimo, MST y orden topológico.
- [ ] Justifiqué alternativas descartadas.
- [ ] Documenté dos reutilizaciones.
- [ ] Agregué ocho pruebas distintivas explicadas.
- [ ] Guardé la salida completa de `pytest -v`.
- [ ] No agregué cachés.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| notebook.md y diagnóstico de problemas | 20 |
| Motor de decisión y contratos | 20 |
| Justificación de alternativas descartadas | 15 |
| Reutilización y adaptación | 15 |
| Pruebas distintivas propias | 15 |
| Comunicación y trabajo en equipo | 10 |
| Reflexión final y GitHub | 5 |
| **Total** | **100** |

