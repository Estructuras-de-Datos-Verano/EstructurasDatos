from __future__ import annotations

import pytest

from implementacion import (
    DecisionAlgoritmica,
    PerfilProblema,
    es_aplicable,
    evaluar_propuesta,
    explicar_descarte,
    seleccionar_estrategia,
    validar_perfil,
)


@pytest.mark.parametrize(
    ("perfil", "algoritmo", "estructura", "operacion", "complejidad"),
    [
        (PerfilProblema("camino_minimo", False, "sin_pesos"), "BFS", "cola", "capas", "O(V+E)"),
        (PerfilProblema("camino_minimo", True, "cero_uno"), "0-1 BFS", "deque", "0/1", "O(V+E)"),
        (PerfilProblema("camino_minimo", True, "no_negativos"), "Dijkstra", "heap", "distancia", "log V"),
        (PerfilProblema("conexion_minima", False, "no_negativos"), "Kruskal", "Union-Find", "componentes", "E log E"),
        (PerfilProblema("orden_dependencias", True, "sin_pesos"), "Kahn", "cola + grados de entrada", "grado de entrada cero", "O(V+E)"),
    ],
)
def test_selecciones_fundamentales(perfil, algoritmo, estructura, operacion, complejidad):
    decision = seleccionar_estrategia(perfil)
    assert isinstance(decision, DecisionAlgoritmica)
    assert decision.algoritmo == algoritmo
    assert decision.estructura == estructura
    assert operacion in decision.operacion_dominante
    assert complejidad in decision.complejidad
    assert decision.advertencia == ""


def test_bfs_admite_grafo_dirigido_y_no_dirigido():
    assert seleccionar_estrategia(PerfilProblema("camino_minimo", True, "sin_pesos")).algoritmo == "BFS"
    assert seleccionar_estrategia(PerfilProblema("camino_minimo", False, "sin_pesos")).algoritmo == "BFS"


def test_kruskal_admite_pesos_negativos():
    decision = seleccionar_estrategia(PerfilProblema("conexion_minima", False, "incluye_negativos"))
    assert decision.algoritmo == "Kruskal"


@pytest.mark.parametrize(
    "perfil",
    [
        PerfilProblema("camino_minimo", True, "incluye_negativos"),
        PerfilProblema("conexion_minima", True, "no_negativos"),
        PerfilProblema("conexion_minima", False, "sin_pesos"),
        PerfilProblema("orden_dependencias", False, "sin_pesos"),
        PerfilProblema("orden_dependencias", True, "no_negativos"),
    ],
)
def test_reconoce_fuera_del_alcance_sin_inventar_algoritmo(perfil):
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo is None
    assert decision.estructura is None
    assert decision.complejidad is None
    assert decision.advertencia


@pytest.mark.parametrize(
    "perfil",
    [
        PerfilProblema("otro", True, "sin_pesos"),
        PerfilProblema("camino_minimo", True, "decimales"),
    ],
)
def test_rechaza_vocabulario_desconocido(perfil):
    with pytest.raises(ValueError):
        validar_perfil(perfil)


@pytest.mark.parametrize(
    "perfil",
    [
        None,
        {"objetivo": "camino_minimo"},
        PerfilProblema(1, True, "sin_pesos"),
        PerfilProblema("camino_minimo", 1, "sin_pesos"),
        PerfilProblema("camino_minimo", True, 0),
    ],
)
def test_rechaza_tipos_invalidos(perfil):
    with pytest.raises(TypeError):
        validar_perfil(perfil)


def test_es_aplicable_compara_con_el_contrato_completo():
    perfil = PerfilProblema("camino_minimo", True, "cero_uno")
    assert es_aplicable("0-1 BFS", perfil)
    assert not es_aplicable("BFS", perfil)
    assert not es_aplicable("Dijkstra", perfil)


def test_explicar_descarte_nombra_limite_y_recomendacion():
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    texto = explicar_descarte("BFS", perfil)
    assert "número de aristas" in texto
    assert "Dijkstra" in texto


def test_explicar_algoritmo_correcto_confirma_operacion():
    texto = explicar_descarte("Kahn", PerfilProblema("orden_dependencias", True, "sin_pesos"))
    assert "sí aplica" in texto and "grado de entrada cero" in texto


def test_evaluar_propuesta_correcta():
    perfil = PerfilProblema("conexion_minima", False, "no_negativos")
    assert evaluar_propuesta(perfil, "Kruskal", "Union-Find") == (True, [])


def test_evaluar_propuesta_detecta_algoritmo_y_estructura():
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    valida, errores = evaluar_propuesta(perfil, "BFS", "cola")
    assert not valida and len(errores) == 2
    assert any("Dijkstra" in error for error in errores)
    assert any("heap" in error for error in errores)


def test_evaluar_propuesta_fuera_de_alcance_no_la_acepta():
    perfil = PerfilProblema("camino_minimo", True, "incluye_negativos")
    valida, errores = evaluar_propuesta(perfil, "Dijkstra", "heap")
    assert not valida and "pesos negativos" in errores[0]


@pytest.mark.parametrize("algoritmo", ["Bellman-Ford", "A*", "", 3])
def test_rechaza_algoritmo_no_estudiado_o_tipo_invalido(algoritmo):
    perfil = PerfilProblema("camino_minimo", True, "sin_pesos")
    excepcion = TypeError if not isinstance(algoritmo, str) else ValueError
    with pytest.raises(excepcion):
        es_aplicable(algoritmo, perfil)


def test_perfil_y_decision_son_inmutables():
    perfil = PerfilProblema("camino_minimo", False, "sin_pesos")
    decision = seleccionar_estrategia(perfil)
    with pytest.raises(Exception):
        perfil.objetivo = "otro"
    with pytest.raises(Exception):
        decision.algoritmo = "otro"

#1-4.
@pytest.mark.parametrize(
    ("perfil", "algoritmo_propuesto", "estructura_propuesta", "esperado_algoritmo", "esperado_estructura"),
    [
        # 1. BFS vs Dijkstra
        (PerfilProblema("camino_minimo", True, "no_negativos"), "BFS", "cola", "Dijkstra", "heap"),
        # 2. 0-1 BFS vs BFS
        (PerfilProblema("camino_minimo", True, "cero_uno"), "BFS", "cola", "0-1 BFS", "deque"),
        # 3. Dijkstra vs Kruskal
        (PerfilProblema("conexion_minima", False, "no_negativos"), "Dijkstra", "heap", "Kruskal", "Union-Find"),
        # 4. BFS vs Kahn
        (PerfilProblema("orden_dependencias", True, "sin_pesos"), "BFS", "cola", "Kahn", "grados de entrada"),
    ],
)
def test_evaluar_propuesta_rechaza_selecciones_incorrectas(perfil, algoritmo_propuesto, estructura_propuesta, esperado_algoritmo, esperado_estructura):
    valida, errores = evaluar_propuesta(perfil, algoritmo_propuesto, estructura_propuesta)

    """
    ## 1. BFS vs Dijkstra

    **Regla:** Para encontrar un camino mínimo en un grafo donde los tramos tienen costos variables que no son negativos, se requiere extraer el mínimo costo acumulado, no procesar por capas.
    **Entrada:** `PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="no_negativos")`. Propuesta: `algoritmo="BFS"`, `estructura="cola"`.
    **Resultado esperado:** `evaluar_propuesta` devuelve `False` y dos mensajes de error: "Algoritmo incorrecto. Se esperaba 'Dijkstra'..." y "Estructura incorrecta. Se esperaba 'heap'...".
    **Alternativa descartada:** BFS. Como indica `explicar_descarte`, BFS asume un costo uniforme (solo minimiza aristas).
    **Relevancia:** Asegura que el usuario no asuma que todos los caminos mínimos se resuelven igual; un peso diferente a 1 rompe la lógica de BFS y exige un Heap.


    ## 2. 0-1 BFS vs BFS

    **Regla:** Un problema de camino mínimo cuyos pesos pertenecen estrictamente al dominio {0, 1} debe aprovechar una optimización específica en lugar de una búsqueda por niveles estándar.
    **Entrada:** `PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="cero_uno")`. Propuesta: `algoritmo="BFS"`, `estructura="cola"`.
    **Resultado esperado:** `evaluar_propuesta` devuelve `False` indicando que se esperaba el algoritmo `0-1 BFS` apoyado en la estructura `deque`.
    **Alternativa descartada:** BFS convencional. Aunque daría una respuesta con adaptaciones, desperdicia la eficiencia de colocar los pesos 0 al frente y los 1 al fondo del deque.
    **Relevancia:** Demuestra que clasificar finamente el dominio de los pesos permite usar estructuras de datos (deque) que reducen la complejidad temporal frente a un Dijkstra, y mejoran la precisión frente a un BFS.


    ## 3. Dijkstra vs Kruskal

    **Regla:** Si el objetivo es conectar globalmente toda la red al menor costo, calcular el costo acumulativo desde un origen hacia los demás nodos no resuelve el problema.
    **Entrada:** `PerfilProblema(objetivo="conexion_minima", dirigido=False, tipo_pesos="no_negativos")`. Propuesta: `algoritmo="Dijkstra"`, `estructura="heap"`.
    **Resultado esperado:** `evaluar_propuesta` devuelve `False` indicando que se esperaba `Kruskal` y la estructura `Union-Find`.
    **Alternativa descartada:** Dijkstra. `explicar_descarte` confirmaría que Dijkstra busca rutas individuales, no redes globales (MST).
    **Relevancia:** Obliga a distinguir entre el "bien individual" (camino mínimo) y el "bien común" (árbol de expansión mínima), evitando elegir Dijkstra solo porque el enunciado dice "menor costo".

    -
    ## 4. BFS vs Kahn

    *   **Regla:** Aunque dos algoritmos usen una cola como estructura base, su invariante y el tipo de problema que resuelven son totalmente distintos.
    *   **Entrada:** `PerfilProblema(objetivo="orden_dependencias", dirigido=True, tipo_pesos="sin_pesos")`. Propuesta: `algoritmo="BFS"`, `estructura="cola"`.
    *   **Resultado esperado:** `evaluar_propuesta` devuelve `False` indicando que el algoritmo esperado es `Kahn` y la estructura exacta es `cola + grados de entrada`.
    *   **Alternativa descartada:** BFS. Mientras BFS encola vecinos descubiertos, Kahn requiere procesar una métrica extra: liberar nodos cuyo grado de entrada llega a cero.
    *   **Relevancia:** Enseña que identificar la estructura principal no exime de identificar la *operación dominante* correcta (liberar dependencias vs procesar capas).

    """
    
    assert not valida
    assert len(errores) == 2
    assert any(esperado_algoritmo in error for error in errores)
    assert any(esperado_estructura in error for error in errores)


# 5. pesos negativos fuera del alcance
def test_pesos_negativos_fuera_del_alcance_rechazados():
    
    """
    ## 5. Pesos negativos fuera del alcance
    **Regla:** Intentar buscar un camino mínimo con costos negativos rompe los invariantes de los algoritmos de la currícula de este código, por lo que debe rechazarse explícitamente.
    **Entrada:** `PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="incluye_negativos")`. Propuesta: `algoritmo="Dijkstra"`, `estructura="heap"`.
    **Resultado esperado:** `evaluar_propuesta` devuelve `False` con el mensaje: "Propuesta inválida: El perfil contiene pesos negativos para camino mínimo, que está fuera de alcance".
    **Alternativa descartada:** Dijkstra. `explicar_descarte` señala que un peso negativo rompe su invariante, porque un camino ya extraído podría abaratarse después.
    **Relevancia:** Es vital que un ingeniero sepa decir "no se puede con mis herramientas actuales" antes de entregar un resultado defectuoso en un sistema en producción.
    """

    perfil = PerfilProblema("camino_minimo", True, "incluye_negativos")
    valida, errores = evaluar_propuesta(perfil, "Dijkstra", "heap")
    
    assert not valida
    assert len(errores) > 0
    assert "pesos negativos" in errores[0].lower() or "fuera de alcance" in errores[0].lower()


# 6. Kruskal con peso negativo
def test_kruskal_acepta_pesos_negativos_sin_romper_invariante():
    """
    ## 6. Kruskal con peso negativo

   **Regla:** A diferencia de Dijkstra, el algoritmo de Kruskal evalúa las aristas de forma global ordenándolas; por tanto, los pesos negativos no rompen su invariante siempre que busque un MST.
   **Entrada:** `PerfilProblema(objetivo="conexion_minima", dirigido=False, tipo_pesos="incluye_negativos")`. Propuesta: `algoritmo="Kruskal"`, `estructura="Union-Find"`.
   **Resultado esperado:** `evaluar_propuesta` devuelve `(True, [])`. La evaluación es exitosa.
   **Alternativa descartada:** Descartar Kruskal por miedo a los pesos negativos.
   **Relevancia:** Demuestra comprensión profunda: los pesos negativos no "rompen los grafos", solo rompen algoritmos que asumen acumulación monótona (Dijkstra), dejando intactos los basados en ordenamiento global (Kruskal).
    """
    perfil = PerfilProblema("conexion_minima", False, "incluye_negativos")
    valida, errores = evaluar_propuesta(perfil, "Kruskal", "Union-Find")
    
    assert valida
    assert len(errores) == 0


# 7. error solo de estructura
def test_error_solo_de_estructura_es_detectado():
   
    """
    ## 7. Error solo de estructura
    **Regla:** Conocer el nombre del algoritmo correcto es inútil si no se implementa sobre la estructura de datos que abarata su operación dominante.
    **Entrada:** `PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="no_negativos")`. Propuesta: `algoritmo="Dijkstra"`, `estructura="cola"`.
    **Resultado esperado:** `evaluar_propuesta` devuelve `False` y una única advertencia: "Estructura incorrecta. Se esperaba 'heap' pero se propuso 'cola'".
    **Alternativa descartada:** La estructura "cola" regular.
    **Relevancia:** Refuerza la lección fundamental de la materia: el algoritmo y la estructura de datos son inseparables. Dijkstra sin Heap degenera su complejidad.
    """


    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    valida, errores = evaluar_propuesta(perfil, "Dijkstra", "cola") 
    
    assert not valida
    assert len(errores) == 1
    assert "Estructura incorrecta" in errores[0]
    assert "Algoritmo incorrecto" not in errores[0]


# 8. perfil inválido
def test_rechaza_perfil_con_vocabulario_invalido():
    """
    ## 8. Perfil inválido

    **Regla:** El código debe protegerse contra dominios léxicos no reconocidos, validando la entrada y los contratos antes de ejecutar cualquier lógica de decisión.
    **Entrada:** `PerfilProblema(objetivo="ruta_mas_corta", dirigido=True, tipo_pesos="enteros")`. (Se usan strings que no están en `OBJETIVOS` ni `TIPOS_PESO`).
    **Resultado esperado:** Al llamar a `validar_perfil` (ya sea directo o mediante otra función), se lanza un `ValueError: Objetivo desconocido: ruta_mas_corta`.
    **Alternativa descartada:** Devolver `None` silenciosamente o intentar adivinar mediante un `else` genérico.
    **Relevancia:** Fomenta la programación defensiva. Si el contrato de entrada se viola, el sistema debe "fallar rápido" (fail-fast) en lugar de propagar estados inválidos o silenciosos.
    """
    perfil = PerfilProblema("ruta_mas_corta", True, "enteros")
    
    with pytest.raises(ValueError, match="Objetivo desconocido"):
        validar_perfil(perfil)