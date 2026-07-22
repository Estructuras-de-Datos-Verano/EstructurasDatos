import math
import pytest
from implementacion import UnionFind, kruskal, costo_reparacion

def test_estudiante_1_union_efectiva():
    """
    REGLA: La unión de dos elementos en componentes distintas debe devolver True,
           reducir el número de componentes en 1 y actualizar el tamaño.
    ENTRADA: UnionFind de 3 elementos. Operación union(0, 1).
    RESULTADO ESPERADO: Retorna True, componentes pasa de 3 a 2, tamano_componente(0) es 2.
    RAZÓN: Al estar desconectados inicialmente, unirlos es una operación efectiva.
    """
    uf = UnionFind(3)
    assert uf.numero_componentes() == 3
    
    # Unión efectiva
    assert uf.union(0, 1) is True
    assert uf.numero_componentes() == 2
    assert uf.tamano_componente(0) == 2


def test_estudiante_2_union_repetida():
    """
    REGLA: La unión de dos elementos que ya pertenecen al mismo conjunto (directa 
           o indirectamente) debe devolver False y no alterar el estado de componentes.
    ENTRADA: UnionFind de 3 elementos. Operaciones: union(0, 1), luego union(1, 0) y union(0, 0).
    RESULTADO ESPERADO: Las uniones repetidas/reflexivas retornan False; el número de componentes se mantiene en 2.
    RAZÓN: Evita que uniones redundantes alteren erróneamente los contadores e invariantes de la estructura.
    """
    uf = UnionFind(3)
    uf.union(0, 1)
    componentes_antes = uf.numero_componentes()
    
    # Uniones redundantes
    assert uf.union(1, 0) is False
    assert uf.union(0, 0) is False
    assert uf.numero_componentes() == componentes_antes


def test_estudiante_3_transitividad():
    """
    REGLA: Si A se une con B, y B se une con C, entonces A y C deben estar conectados.
    ENTRADA: UnionFind de 4 elementos. Operaciones: union(0, 1), union(1, 2).
    RESULTADO ESPERADO: conectados(0, 2) debe ser True.
    RAZÓN: La conectividad es una relación de equivalencia transitiva manejada correctamente por las raíces.
    """
    uf = UnionFind(4)
    uf.union(0, 1)
    uf.union(1, 2)
    assert uf.conectados(0, 2) is True


def test_estudiante_4_tamano_componente():
    """
    REGLA: El tamaño de la componente debe poder consultarse desde cualquier elemento
           perteneciente a ella y reflejar el total acumulado de nodos.
    ENTRADA: UnionFind de 5 elementos. Unimos (0, 1) y luego (2, 3), y finalmente (1, 3).
    RESULTADO ESPERADO: tamano_componente(0) == 4, tamano_componente(3) == 4.
    RAZÓN: La unión por tamaño acumula los nodos en la raíz de manera coherente.
    """
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(1, 3)
    assert uf.tamano_componente(0) == 4
    assert uf.tamano_componente(3) == 4


def test_estudiante_5_arista_rechazada_por_ciclo():
    """
    REGLA: Kruskal debe ignorar y rechazar aristas que conectan nodos que ya están
           en la misma componente para evitar la formación de ciclos.
    ENTRADA: Triángulo de 3 vértices: [(0, 1, 1), (1, 2, 2), (0, 2, 5)].
    RESULTADO ESPERADO: El MST final solo contiene las aristas (0, 1) y (1, 2) con costo total 3.0.
    RAZÓN: La arista (0, 2) con peso 5 se rechaza porque cerraría un ciclo.
    """
    aristas = [(0, 1, 1), (1, 2, 2), (0, 2, 5)]
    resultado = kruskal(3, aristas)
    assert resultado is not None
    costo, elegidas = resultado
    assert costo == 3.0
    assert len(elegidas) == 2
    # El set de aristas seleccionadas no debe tener la arista (0, 2)
    assert (0, 2, 5.0) not in elegidas


def test_estudiante_6_grafo_desconectado():
    """
    REGLA: Si el grafo de entrada no es conectado, no es posible construir un árbol
           de expansión que abarque todos los vértices, por lo que debe retornar None.
    ENTRADA: 4 vértices con aristas [(0, 1, 1), (2, 3, 2)].
    RESULTADO ESPERADO: kruskal retorna None.
    RAZÓN: Se procesan todas las aristas y el número de seleccionadas es menor a V-1.
    """
    aristas = [(0, 1, 1), (2, 3, 2)]
    assert kruskal(4, aristas) is None


def test_estudiante_indice_negativo_lanza_error():
    """Verifica que el contrato de UnionFind lance IndexError con índices negativos."""
    uf = UnionFind(5)
    with pytest.raises(IndexError):
        uf.find(-1)
    with pytest.raises(IndexError):
        uf.union(0, -5)


def test_estudiante_bool_como_indice_lanza_error():
    """Python evalúa bool como subclase de int. Debemos validar que lance TypeError."""
    uf = UnionFind(5)
    with pytest.raises(TypeError):
        uf.find(True)
    with pytest.raises(TypeError):
        uf.union(False, 2)


def test_estudiante_compresion_de_caminos():
    """Verifica que 'find' aplane el árbol interno sin alterar la estructura lógica."""
    uf = UnionFind(4)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)
    
    # El camino se comprime al llamar a find
    raiz = uf.find(3)
    assert uf._padre[3] == raiz
    assert uf._padre[2] == raiz
    assert uf.numero_componentes() == 1


def test_estudiante_kruskal_pesos_negativos():
    """Kruskal debe admitir pesos negativos y ordenarlos correctamente."""
    aristas = [(0, 1, -10), (1, 2, -5), (0, 2, 0)]
    resultado = kruskal(3, aristas)
    assert resultado is not None
    costo, elegidas = resultado
    assert costo == -15.0
    assert len(elegidas) == 2


def test_estudiante_kruskal_no_mutacion():
    """Verifica que la lista original de aristas de entrada no sea alterada (ordenada in-place)."""
    aristas = [(0, 1, 10), (1, 2, 2), (0, 2, 5)]
    copia = aristas.copy()
    
    kruskal(3, aristas)
    assert aristas == copia


def test_estudiante_road_reparation_impossible():
    """Prueba que costo_reparacion devuelva None si es imposible conectar la red."""
    # 3 ciudades, pero solo hay carretera entre 0 y 1. La ciudad 2 queda huérfana.
    carreteras = [(0, 1, 10)]
    assert costo_reparacion(3, carreteras) is None
