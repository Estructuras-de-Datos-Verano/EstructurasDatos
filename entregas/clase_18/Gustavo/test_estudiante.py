"""Pruebas propias del estudiante para Union-Find y Kruskal."""

import pytest
from entregas.clase_18.Gustavo.implementacion import UnionFind, kruskal

def test_union_efectiva_reduce_componentes():
    """
    Regla: Al unir dos elementos de componentes distintas, la unión es efectiva y 
           el contador total de componentes debe disminuir en 1.
    Entrada: UnionFind(3), se llama a union(0, 1).
    Resultado Esperado: union(0, 1) devuelve True y numero_componentes() devuelve 2.
    Razón: 0 y 1 inician como componentes aisladas. Al unirlas exitosamente, pasan a ser 
           un solo conjunto, reduciendo el total de 3 a 2.
    """
    uf = UnionFind(3)
    assert uf.numero_componentes() == 3
    assert uf.union(0, 1) is True
    assert uf.numero_componentes() == 2

def test_union_repetida_no_altera_estado():
    """
    Regla: Intentar unir dos elementos que ya pertenecen a la misma componente 
           no debe tener efecto y debe devolver False.
    Entrada: uf.union(0, 1) y luego uf.union(1, 0) en un UnionFind de 3 elementos.
    Resultado Esperado: El segundo union devuelve False y los tamaños/contador no cambian.
    Razón: El enlace ya existe. La estructura evita ciclos al detectarlo y descarta 
           la operación redundante de inmediato.
    """
    uf = UnionFind(3)
    assert uf.union(0, 1) is True
    antes = uf.numero_componentes()
    
    assert uf.union(1, 0) is False
    assert uf.numero_componentes() == antes
    assert uf.tamano_componente(0) == 2

def test_transitividad_entre_componentes():
    """
    Regla: La conectividad es transitiva. Si A está conectado con B, y B con C, 
           entonces A está conectado con C.
    Entrada: uf.union(0, 1) y uf.union(1, 2).
    Resultado Esperado: conectados(0, 2) debe devolver True.
    Razón: Aunque no se unieron 0 y 2 directamente, al compartir la misma raíz (gracias 
           a las fusiones previas), la estructura los reconoce como el mismo grupo.
    """
    uf = UnionFind(4)
    uf.union(0, 1)
    uf.union(1, 2)
    assert uf.conectados(0, 2) is True

def test_tamano_componente_se_acumula():
    """
    Regla: El tamaño de una componente debe ser la suma de los tamaños de 
           los conjuntos que se fusionan.
    Entrada: Se unen (0,1) y luego (2,3). Finalmente se unen (1,3).
    Resultado Esperado: tamano_componente(0) devuelve 4.
    Razón: Se fusionan dos subárboles independientes de tamaño 2. La unión por tamaño 
           garantiza que la nueva raíz reporte correctamente la suma total (4).
    """
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(1, 3)
    
    # Comprobamos en cualquier nodo del grupo, gracias a la búsqueda de raíz interna
    assert uf.tamano_componente(0) == 4
    assert uf.tamano_componente(2) == 4

def test_kruskal_rechaza_arista_por_ciclo():
    """
    Regla: Kruskal debe omitir aristas que, al agregarse, conecten nodos de 
           la misma componente (formando un ciclo).
    Entrada: 3 vértices en forma de triángulo: [(0,1,1), (1,2,2), (0,2,3)].
    Resultado Esperado: El costo total es 3.0 y solo se eligen 2 aristas (la de peso 3 se ignora).
    Razón: Las primeras dos aristas ordenadas (peso 1 y 2) conectan todo el grafo (V-1 = 2). 
           La arista (0, 2) con peso 3 cerraría el ciclo, por lo que union() devuelve False.
    """
    aristas = [(0, 1, 1), (1, 2, 2), (0, 2, 3)]
    resultado = kruskal(3, aristas)
    
    assert resultado is not None
    costo, elegidas = resultado
    assert costo == 3.0
    assert len(elegidas) == 2
    # Aseguramos que la arista pesada fue ignorada
    assert (0, 2, 3.0) not in elegidas

def test_kruskal_detecta_grafo_desconectado():
    """
    Regla: Si tras procesar todas las aristas no se alcanzan V-1 selecciones, 
           no existe un árbol de expansión que cubra la red.
    Entrada: 4 vértices y solo 2 aristas [(0,1,1), (2,3,1)].
    Resultado Esperado: Devuelve None.
    Razón: Faltan aristas para conectar las componentes {0,1} y {2,3}. 
           Kruskal termina su bucle con solo 2 aristas seleccionadas, y como necesita 3 (V-1), detecta la desconexión.
    """
    aristas = [(0, 1, 1), (2, 3, 1)]
    resultado = kruskal(4, aristas)
    assert resultado is None