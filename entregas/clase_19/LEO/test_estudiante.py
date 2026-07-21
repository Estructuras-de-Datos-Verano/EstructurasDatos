from implementacion import *


def test_varios_ordenes_validos_con_dos_componentes_LEO():
    """
    Regla: un DAG puede tener varios órdenes topológicos válidos.
    Entrada: dos componentes ajenos A→B y C→D.
    Resultado esperado: el orden obtenido debe ser válido aunque no sea único.
    Relevancia: protege que la implementación no dependa de un único orden esperado.
    """
    grafo = {"A": ["B"], "B": [], "C": ["D"], "D": []}
    orden = orden_topologico(grafo)
    assert orden is not None
    assert es_orden_topologico(grafo, orden)


def test_ciclo_en_un_componente_y_otro_libre_LEO():
    """
    Regla: un ciclo en cualquier componente lanza None
    Entrada: A->b->A forma un ciclo y C->D es acíclico.
    Resultado esperado: la función devuelve None.
    Relevancia: protege que no se devuelvan únicamente los nodos del componente válido.
    """
    grafo = {"A": ["B"], "B": ["A"], "C": ["D"], "D": []}
    assert orden_topologico(grafo) is None


def test_vecino_implicito_solo_aparece_como_destino_LEO():
    """
    Regla: un nodo que solo aparece como destino debe agregarse automáticamente.
    Entrada: A→B donde B no existe como llave
    Resultado esperado: B aparece en el grafo normalizado
    Relevancia: protege que se agreguen vecinos implícitos
    """
    esperado = {"A": ["B"], "B": []}
    assert normalizar_grafo_dirigido({"A": ["B"]}) == esperado


def test_dependencias_duplicadas_no_alteran_grado_LEO():
    """
    Regla: dependencias repetidas cuentan una sola vez
    Entrada: A→B repetida varias veces.
    Resultado esperado: el grado de entrada de B es uno.
    Relevancia: protege la eliminación correcta de duplicados antes del cálcos
    """
    grados = grados_entrada({"A": ["B", "B", "B"]})
    assert grados == {"A": 0, "B": 1}


def test_orden_incorrecto_por_precedencia_LEO():
    """
    Regla: un nodo no puede aparecer antes de alguno de sus prerrequisitos.
    Entrada: A->B->C y el orden C,B,A.
    Resultado esperado: la validación devuelve False.
    Relevancia: protege la comprobación de precedencias entre nodos.
    """
    grafo = {"A": ["B"], "B": ["C"], "C": []}
    assert not es_orden_topologico(grafo, ["C", "B", "A"])



def test_cursos_con_componentes_independientes_LEO():
    """
    Regla: cursos pertenecientes a componentes independientes pueden aparecer en cualquier posición siempre que respeten sus dependencias.
    Entrada: 0->1 y 2->3.
    Resultado esperado: se obtiene un orden válido con los cuarto cursos
    Relevancia: protege que el algoritmo funcione con varios componentes.
    """
    prerrequisitos = [(0, 1), (2, 3)]
    orden = ordenar_cursos(4, prerrequisitos)
    assert orden is not None
    validar_orden_cursos(4, prerrequisitos, orden)