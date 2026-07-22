from math import inf, isinf

import pytest

from implementacion import (
    ColaLigada,
    DequeLigada,
    NodoDoble,
    NodoSimple,
    bfs_camino,
    bfs_predecesores,
    camino_cero_uno,
    cero_uno_bfs,
    reconstruir_camino,
)


def test_exporta_los_dos_tipos_de_nodo():
    assert NodoSimple(3).valor == 3
    assert NodoDoble("A").valor == "A"


def test_cola_comienza_vacia_y_admite_valores_repetidos():
    cola = ColaLigada()
    assert cola.esta_vacia() and len(cola) == 0
    cola.encolar("A")
    cola.encolar("A")
    assert cola.primero() == "A" and len(cola) == 2
    assert [cola.desencolar(), cola.desencolar()] == ["A", "A"]


def test_cola_respeta_fifo_y_tamano():
    cola = ColaLigada()
    for valor in ("A", "B", "C"):
        cola.encolar(valor)
    assert cola.primero() == "A"
    assert len(cola) == 3
    assert [cola.desencolar() for _ in range(3)] == ["A", "B", "C"]
    assert cola.esta_vacia()


def test_cola_vacia_falla_y_puede_reutilizarse():
    cola = ColaLigada()
    with pytest.raises(IndexError):
        cola.primero()
    with pytest.raises(IndexError):
        cola.desencolar()
    cola.encolar(1)
    assert cola.desencolar() == 1
    cola.encolar(2)
    assert (cola.primero(), cola.desencolar(), len(cola)) == (2, 2, 0)


def test_cola_restaurada_no_conserva_extremos():
    cola = ColaLigada()
    cola.encolar("único")
    retirado = cola._frente
    cola.desencolar()
    assert cola._frente is None and cola._final is None
    assert retirado is not None and retirado.siguiente is None


def test_deque_opera_por_ambos_extremos():
    deque = DequeLigada()
    deque.agregar_final("B")
    deque.agregar_inicio("A")
    deque.agregar_final("C")
    assert (deque.primero(), deque.ultimo(), len(deque)) == ("A", "C", 3)
    assert deque.quitar_inicio() == "A"
    assert deque.quitar_final() == "C"
    assert deque.quitar_inicio() == "B"
    assert deque.esta_vacia()


def test_deque_comienza_vacia_y_admite_valores_repetidos():
    deque = DequeLigada()
    assert deque.esta_vacia() and len(deque) == 0
    deque.agregar_inicio("A")
    deque.agregar_final("A")
    assert deque.primero() == deque.ultimo() == "A"
    assert deque.quitar_inicio() == deque.quitar_final() == "A"


def test_deque_vacia_falla_y_puede_reutilizarse():
    deque = DequeLigada()
    for operacion in (deque.primero, deque.ultimo, deque.quitar_inicio, deque.quitar_final):
        with pytest.raises(IndexError):
            operacion()
    deque.agregar_inicio(1)
    assert deque.quitar_final() == 1
    deque.agregar_final(2)
    assert deque.quitar_inicio() == 2


def test_deque_desconecta_nodos_retirados():
    deque = DequeLigada()
    for valor in (1, 2, 3):
        deque.agregar_final(valor)
    primero = deque._inicio
    ultimo = deque._final
    deque.quitar_inicio()
    deque.quitar_final()
    assert primero is not None and primero.anterior is None and primero.siguiente is None
    assert ultimo is not None and ultimo.anterior is None and ultimo.siguiente is None
    assert deque._inicio is deque._final
    assert deque._inicio is not None
    assert deque._inicio.anterior is None and deque._inicio.siguiente is None


def grafo_bfs():
    return {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "E"],
        "D": ["B", "F"],
        "E": ["B", "C", "F"],
        "F": ["D", "E"],
    }


def test_bfs_conserva_orden_de_vecinos_y_camino_minimo():
    predecesores = bfs_predecesores(grafo_bfs(), "A")
    assert predecesores == {
        "A": None, "B": "A", "C": "A", "D": "B", "E": "B", "F": "D"
    }
    assert bfs_camino(grafo_bfs(), "A", "F") == ["A", "B", "D", "F"]


def test_bfs_identidad_camino_directo_y_direccion():
    grafo = {"A": ["B"], "B": []}
    assert bfs_camino(grafo, "A", "A") == ["A"]
    assert bfs_camino(grafo, "A", "B") == ["A", "B"]
    assert bfs_camino(grafo, "B", "A") == []


def test_bfs_termina_en_un_ciclo_y_deja_inalcanzable_en_none():
    grafo = {"A": ["B"], "B": ["C"], "C": ["A"], "X": []}
    pred = bfs_predecesores(grafo, "A")
    assert pred == {"A": None, "B": "A", "C": "B", "X": None}
    assert bfs_camino(grafo, "A", "X") == []


def test_bfs_incluye_vecino_implicito_y_no_muta_entrada():
    grafo = {"A": ["B"]}
    copia = {nodo: vecinos.copy() for nodo, vecinos in grafo.items()}
    assert bfs_camino(grafo, "A", "B") == ["A", "B"]
    assert grafo == copia and "B" not in grafo


def test_bfs_rechaza_origen_o_destino_ausentes():
    with pytest.raises(KeyError, match="origen"):
        bfs_predecesores({"A": []}, "X")
    with pytest.raises(KeyError, match="destino"):
        bfs_camino({"A": []}, "A", "X")


def test_reconstruir_cubre_identidad_inalcanzable_y_ciclo():
    assert reconstruir_camino({"A": None}, "A", "A") == ["A"]
    assert reconstruir_camino({"A": None, "X": None}, "A", "X") == []
    with pytest.raises(ValueError, match="ciclo"):
        reconstruir_camino({"A": None, "B": "C", "C": "B"}, "A", "B")


def grafo_01():
    return {
        "A": [("B", 0), ("C", 1)],
        "B": [("D", 0), ("E", 1)],
        "C": [("D", 0)],
        "D": [("F", 1)],
        "E": [("F", 0)],
        "F": [],
    }


def test_cero_uno_bfs_calcula_distancias_y_predecesores():
    distancias, pred = cero_uno_bfs(grafo_01(), "A")
    assert distancias == {"A": 0, "B": 0, "C": 1, "D": 0, "E": 1, "F": 1}
    assert pred["B"] == "A" and pred["D"] == "B" and pred["F"] == "D"
    assert camino_cero_uno(grafo_01(), "A", "F") == (1, ["A", "B", "D", "F"])


def test_cero_uno_prefiere_mas_aristas_si_cuestan_menos():
    grafo = {"A": [("X", 1), ("B", 0)], "B": [("C", 0)], "C": [("X", 0)], "X": []}
    assert camino_cero_uno(grafo, "A", "X") == (0, ["A", "B", "C", "X"])


def test_cero_uno_con_solo_pesos_cero():
    grafo = {"A": [("B", 0)], "B": [("C", 0)], "C": []}
    assert camino_cero_uno(grafo, "A", "C") == (0, ["A", "B", "C"])


def test_cero_uno_con_solo_pesos_uno():
    grafo = {"A": [("B", 1)], "B": [("C", 1)], "C": []}
    assert camino_cero_uno(grafo, "A", "C") == (2, ["A", "B", "C"])


def test_cero_uno_actualiza_una_mejora_posterior():
    grafo = {"A": [("X", 1), ("B", 0)], "B": [("C", 0)], "C": [("X", 0)], "X": []}
    distancias, pred = cero_uno_bfs(grafo, "A")
    assert distancias["X"] == 0 and pred["X"] == "C"


def test_cero_uno_identidad_e_inalcanzable():
    grafo = {"A": [], "X": []}
    assert camino_cero_uno(grafo, "A", "A") == (0, ["A"])
    costo, camino = camino_cero_uno(grafo, "A", "X")
    assert isinf(costo) and camino == []


def test_cero_uno_incluye_vecino_implicito_y_no_muta_entrada():
    grafo = {"A": [("B", 0)]}
    copia = {nodo: aristas.copy() for nodo, aristas in grafo.items()}
    distancias, _ = cero_uno_bfs(grafo, "A")
    assert distancias == {"A": 0, "B": 0}
    assert grafo == copia and "B" not in grafo


@pytest.mark.parametrize("peso", [True, False, 0.0, "1", None])
def test_cero_uno_rechaza_peso_de_tipo_incorrecto(peso):
    with pytest.raises(TypeError, match="entero 0 o 1"):
        cero_uno_bfs({"A": [("B", peso)]}, "A")


@pytest.mark.parametrize("peso", [-1, 2, 8])
def test_cero_uno_rechaza_entero_fuera_del_dominio(peso):
    with pytest.raises(ValueError, match="0 o 1"):
        cero_uno_bfs({"A": [("B", peso)]}, "A")


def test_cero_uno_rechaza_forma_y_nodos_invalidos():
    with pytest.raises(ValueError, match="dos elementos"):
        cero_uno_bfs({"A": [("B", 0, "extra")]}, "A")
    with pytest.raises(TypeError, match="vecino"):
        cero_uno_bfs({"A": [(3, 0)]}, "A")
    with pytest.raises(KeyError, match="origen"):
        cero_uno_bfs({"A": []}, "X")
    with pytest.raises(KeyError, match="destino"):
        camino_cero_uno({"A": []}, "A", "X")


def test_constante_infinito_es_compatible_con_contrato():
    distancias, pred = cero_uno_bfs({"A": [], "X": []}, "A")
    assert distancias["X"] == inf and pred["X"] is None

def test_1_cola_ligada_fifo():
    # Regla protegida: Orden de salida estrictamente secuencial FIFO (First-In, First-Out).
    # Entrada: Encolar secuencialmente los elementos "A", luego "B", y por último "C".
    # Resultado esperado: Al desencolar de manera sucesiva, se obtienen "A", "B" y "C" en ese orden exacto.
    # Razón de importancia: Si no se respeta la cola FIFO, el recorrido BFS explorará el grafo en profundidad (como un DFS), arruinando la garantía matemática de encontrar caminos mínimos por número de aristas.
    cola = ColaLigada[str]()
    cola.encolar("A")
    cola.encolar("B")
    cola.encolar("C")
    assert cola.desencolar() == "A"
    assert cola.desencolar() == "B"
    assert cola.desencolar() == "C"
    assert cola.esta_vacia()


def test_2_cola_ligada_reutilizacion_despues_de_vaciarla():
    # Regla protegida: El vaciado total de la estructura debe restaurar limpiamente ambos extremos (frente y final) a None.
    # Entrada: Encolar "A", vaciar la cola mediante desencolar(), y de inmediato volver a encolar un elemento "B".
    # Resultado esperado: La estructura se comporta de forma idéntica en ciclos sucesivos sin heredar basura del estado previo.
    # Razón de importancia: Si el puntero del final no se actualiza o limpia tras quedar vacío, las nuevas inserciones provocarán desconexiones en los nodos o excepciones por atributos nulos.
    cola = ColaLigada[str]()
    cola.encolar("A")
    assert cola.desencolar() == "A"
    assert cola.esta_vacia()
    cola.encolar("B")
    assert cola.desencolar() == "B"
    assert cola.esta_vacia()


def test_3_deque_ligada_operaciones_combinadas():
    # Regla protegida: Coherencia y consistencia bidireccional en flujos concurrentes por ambos extremos de la Deque.
    # Entrada: Insertar "B" al final, "A" al inicio, y "C" al final. Estructura interna resultante: ["A", "B", "C"].
    # Resultado esperado: quitar_inicio() devuelve "A", quitar_final() devuelve "C", y quitar_inicio() devuelve "B".
    # Razón de importancia: El algoritmo 0-1 BFS confía por completo en la validez simultánea de operaciones por la cabeza y la cola en tiempo O(1) para procesar los diferentes pesos sin corromper la memoria.
    deque = DequeLigada[str]()
    deque.agregar_final("B")
    deque.agregar_inicio("A")
    deque.agregar_final("C")
    assert deque.quitar_inicio() == "A"
    assert deque.quitar_final() == "C"
    assert deque.quitar_inicio() == "B"
    assert deque.esta_vacia()


def test_4_deque_ligada_reutilizacion_despues_de_vaciarla():
    # Regla protegida: Desanclaje absoluto y reseteo mutuo de punteros al remover el último elemento de la Deque Ligada.
    # Entrada: Agregar "X" al inicio, removerlo con quitar_final(), luego agregar "Y" al final y removerlo con quitar_inicio().
    # Resultado esperado: Ciclos de limpieza y reinserción transparentes sin fugas de memoria o punteros zombis.
    # Razón de importancia: Evita que nodos eliminados mantengan enlaces residuales que causen ciclos infinitos o comportamientos extraños en ejecuciones posteriores de algoritmos de optimización.
    deque = DequeLigada[str]()
    deque.agregar_inicio("X")
    assert deque.quitar_final() == "X"
    assert deque.esta_vacia()
    deque.agregar_final("Y")
    assert deque.quitar_inicio() == "Y"
    assert deque.esta_vacia()


def test_5_bfs_con_ciclo():
    # Regla protegida: Prevención de bucles infinitos mediante el control estricto de nodos ya visitados en la exploración BFS.
    # Entrada: Grafo circular con un bucle explícito: {"A": ["B"], "B": ["C", "A"], "C": []} buscando ruta desde "A" hasta "C".
    # Resultado esperado: Retorna el camino más corto eludiendo el bucle eterno, resultando en ["A", "B", "C"].
    # Razón de importancia: Una mala gestión de ciclos detiene la CPU en bucles infinitos y genera fallos catastróficos por agotamiento total de recursos en producción.
    grafo = {"A": ["B"], "B": ["C", "A"], "C": []}
    assert bfs_camino(grafo, "A", "C") == ["A", "B", "C"]


def test_6_bfs_con_destino_inalcanzable():
    # Regla protegida: Terminación segura y controlada devolviendo una lista vacía ante la ausencia total de conectividad física.
    # Entrada: Grafo disconexo compuesto por componentes aisladas: {"A": ["B"], "B": [], "C": ["D"], "D": []} buscando de "A" a "C".
    # Resultado esperado: Retorna de forma limpia una lista vacía `[]`.
    # Razón de importancia: Evita errores graves no controlados (como KeyError) o la construcción errónea de rutas fantasma fragmentadas en la interfaz de usuario.
    grafo = {"A": ["B"], "B": [], "C": ["D"], "D": []}
    assert bfs_camino(grafo, "A", "C") == []


def test_7_cero_uno_bfs_con_ruta_de_mas_aristas_pero_menor_costo():
    # Regla protegida: Priorización absoluta del costo acumulado sobre la cantidad lineal de aristas transitadas.
    # Entrada: Ruta directa pero cara (A->B costo 1) vs Ruta larga pero totalmente gratis (A->C->D->B costo 0).
    # Grafo: {"A": [("B", 1), ("C", 0)], "C": [("D", 0)], "D": [("B", 0)], "B": []} buscando de "A" a "B".
    # Resultado esperado: Costo total igual a 0.0 y un camino óptimo largo integrado por ["A", "C", "D", "B"].
    # Razón de importancia: Valida que la estrategia de inserción preferencial al inicio (costo 0) ordene la Deque adecuadamente, superando la miopía del BFS convencional.
    grafo = {
        "A": [("B", 1), ("C", 0)],
        "C": [("D", 0)],
        "D": [("B", 0)],
        "B": []
    }
    costo, camino = camino_cero_uno(grafo, "A", "B")
    assert costo == 0.0
    assert camino == ["A", "C", "D", "B"]


def test_8_cero_uno_bfs_con_peso_invalido():
    # Regla protegida: Validación del dominio de tipos y exclusión estricta de booleanos camuflados en las sumas aritméticas.
    # Entrada: Grafo que contiene una arista corrupta con peso de tipo booleano: {"A": [("B", True)]}.
    # Resultado esperado: Se levanta de inmediato una excepción TypeError indicando explícitamente que se esperaba un entero.
    # Razón de importancia: En Python, `True` es una subclase de `int` (`True == 1`). Omitir esta validación causaría que el algoritmo asimile el booleano en silencio y devuelva costos distorsionados.
    grafo = {"A": [("B", True)]}
    with pytest.raises(TypeError, match="entero 0 o 1"):
        cero_uno_bfs(grafo, "A")


# ------------------------------------------------------------------------------
# Casos recomendados adicionales (Casos frontera y robustez)
# ------------------------------------------------------------------------------

def test_9_origen_igual_destino():
    # Regla protegida: Resolución inmediata en O(1) de caminos triviales sin costo operativo.
    # Entrada: Origen "A" y Destino "A" sobre un grafo cualquiera.
    # Resultado esperado: bfs_camino devuelve ["A"] y camino_cero_uno devuelve (0.0, ["A"]).
    # Razón de importancia: Asegura que el algoritmo sea resiliente ante búsquedas redundantes que inician en la meta sin alterar las libretas.
    grafo = {"A": []}
    assert bfs_camino(grafo, "A", "A") == ["A"]
    costo, camino = camino_cero_uno({"A": []}, "A", "A")
    assert costo == 0.0
    assert camino == ["A"]


def test_10_vecino_implicito_en_nodos_sumidero():
    # Regla protegida: Descubrimiento dinámico de nodos de salida que no aparecen explícitamente como llaves del diccionario.
    # Entrada: Grafo {"A": [("B", 0)]} donde "B" no posee una entrada principal de adyacencia en el mapeo de entrada.
    # Resultado esperado: Inicialización automática de distancias para "B" a infinito sin provocar una excepción KeyError.
    # Razón de importancia: En los grafos reales, los nodos sumidero comúnmente se omiten como llaves; el inicializador debe mapearlos dinámicamente escaneando las listas de adyacencia.
    grafo = {"A": [("B", 0)]}
    distancias, _ = cero_uno_bfs(grafo, "A")
    assert "B" in distancias
    assert distancias["B"] == 0.0


def test_11_no_mutacion_del_grafo_usuario():
    # Regla protegida: Garantía de operaciones puras de sólo lectura sobre las estructuras de datos suministradas por el cliente.
    # Entrada: Grafo estructurado original {"A": [("B", 1)], "B": []} y una copia de control exacta.
    # Resultado esperado: Tras invocar el algoritmo de enrutamiento completo, el grafo original se conserva inalterado.
    # Razón de importancia: Modificar de forma colateral los parámetros provistos por el usuario provoca errores colosales y bugs difíciles de rastrear en otros módulos paralelos del ecosistema informático.
    grafo = {"A": [("B", 1)], "B": []}
    respaldo = {"A": [("B", 1)], "B": []}
    cero_uno_bfs(grafo, "A")
    assert grafo == respaldo


def test_12_mejora_posterior_de_caminos_ya_descubiertos():
    # Regla protegida: Capacidad de actualizar y optimizar dinámicamente distancias y padres ante el hallazgo tardío de rutas más económicas.
    # Entrada: El nodo "B" es descubierto en primera instancia con un costo subóptimo de 1 a través de la arista directa; más tarde se halla una ruta por "C" con costo acumulado final de 0.
    # Grafo: {"A": [("B", 1), ("C", 0)], "C": [("B", 0)], "B": []}
    # Resultado esperado: La distancia final de "B" se corrige a 0.0 y su predecesor cambia exitosamente de "A" a "C".
    # Razón de importancia: Es la esencia del 0-1 BFS; de fallar la actualización condicional, el algoritmo perdería atajos óptimos descubiertos después de la primera impresión.
    grafo = {
        "A": [("B", 1), ("C", 0)],
        "C": [("B", 0)],
        "B": []
    }
    distancias, predecesores = cero_uno_bfs(grafo, "A")
    assert distancias["B"] == 0.0
    assert predecesores["B"] == "C"