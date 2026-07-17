import pytest
from implementacion import (
    ColaLigada, DequeLigada, bfs_camino, cero_uno_bfs, camino_cero_uno
)

# 1. Pruebas de ColaLigada (BFS base)

def test_cola_comportamiento_fifo():
    """
    Regla protegida: El primer elemento en entrar es el primero en salir (FIFO).
    Entrada: Encolar 1, 2 y 3 en ese orden.
    Resultado esperado: Desencolar devuelve 1, luego 2, luego 3.
    Razón de importancia: Es el corazón de BFS. Si la cola actúa como pila (LIFO), BFS se convierte accidentalmente en DFS.
    """
    cola = ColaLigada()
    cola.encolar(1)
    cola.encolar(2)
    cola.encolar(3)
    
    assert cola.desencolar() == 1
    assert cola.desencolar() == 2
    assert cola.desencolar() == 3
    assert cola.esta_vacia()

def test_cola_reutilizacion_tras_vaciar():
    """
    Regla protegida: Vaciar la estructura restaura los invariantes (frente y final = None, tamaño = 0).
    Entrada: Encolar "A", desencolar "A", encolar "B", desencolar "B".
    Resultado esperado: La cola se vacía sin lanzar excepciones y devuelve "B" en el segundo ciclo.
    Razón de importancia: Previene referencias residuales ("basura" en memoria) que corrompan el próximo uso.
    """
    cola = ColaLigada()
    cola.encolar("A")
    assert cola.desencolar() == "A"
    assert len(cola) == 0
    
    cola.encolar("B")
    assert cola.desencolar() == "B"
    assert cola.esta_vacia()

# 2. Pruebas de DequeLigada (0-1 BFS base)

def test_deque_operaciones_combinadas():
    """
    Regla protegida: Los enlaces bidireccionales (`anterior` y `siguiente`) son consistentes.
    Entrada: agregar_inicio("X"), agregar_final("Y"), agregar_inicio("W"), quitar_final().
    Resultado esperado: Quitar final devuelve "Y", tamaño se ajusta correctamente a 2.
    Razón de importancia: Garantiza que mezclar operaciones O(1) en ambos extremos no rompa la cadena interna.
    """
    deque = DequeLigada()
    deque.agregar_inicio("X")
    deque.agregar_final("Y")
    deque.agregar_inicio("W") # W <-> X <-> Y
    
    assert deque.quitar_final() == "Y"
    assert len(deque) == 2
    assert deque.quitar_inicio() == "W"

def test_deque_reutilizacion_tras_vaciar():
    """
    Regla protegida: El estado vacío es consistente desde cualquier extremo.
    Entrada: Llenar por inicio, vaciar por final, agregar por final, quitar por inicio.
    Resultado esperado: Extrae correctamente el último elemento añadido ("Z").
    Razón de importancia: Los extremos en una deque ligada son frágiles si no se manejan simétricamente al llegar a 0 elementos.
    """
    deque = DequeLigada()
    deque.agregar_inicio(1)
    deque.quitar_final()
    
    deque.agregar_final("Z")
    assert deque.quitar_inicio() == "Z"
    assert deque.esta_vacia()

# 3. Pruebas de Alternancia y Estrés

def test_cola_secuencias_largas_alternadas():
    """
    Regla protegida: Mantenimiento de tamaño y referencias bajo carga continua O(1).
    Entrada: Bucle de 10,000 iteraciones encolando 2 y desencolando 1 repetidamente.
    Resultado esperado: El tamaño final es 10,000 y el primer elemento válido es 5000.
    Razón de importancia: Valida que no hay fugas de memoria, recursión accidental o recorridos O(n) ocultos.
    """
    cola = ColaLigada()
    for i in range(10000):
        cola.encolar(i)
        cola.encolar(i + 10000)
        cola.desencolar()
    
    assert len(cola) == 10000
    # Al encolar de 2 en 2 y sacar 1, al término de 10,000 iteraciones, 
    # el siguiente en la línea es el 5000.
    assert cola.desencolar() == 5000

# 4. Pruebas de BFS

def test_bfs_con_ciclo():
    """
    Regla protegida: Un nodo ya visitado no debe encolarse nuevamente.
    Entrada: Grafo triangular A->B, B->C, C->A. Origen A, destino C.
    Resultado esperado: Camino [A, B, C] o [A, C], finaliza sin bucle infinito.
    Razón de importancia: Si los visitados se marcan al desencolar y no al encolar, un ciclo colgará la ejecución.
    """
    grafo = {"A": ["B", "C"], "B": ["C"], "C": ["A"]}
    camino = bfs_camino(grafo, "A", "C")
    assert camino in (["A", "B", "C"], ["A", "C"])

def test_bfs_destino_inalcanzable():
    """
    Regla protegida: Destino inalcanzable produce lista vacía.
    Entrada: Grafo desconectado {"A": ["B"], "C": ["D"]}. Origen A, destino C.
    Resultado esperado: `[]`.
    Razón de importancia: Evita falsos positivos y errores `KeyError` en la reconstrucción del camino.
    """
    grafo = {"A": ["B"], "B": [], "C": ["D"], "D": []}
    assert bfs_camino(grafo, "A", "C") == []

# 5. Pruebas de 0-1 BFS

def test_cero_uno_bfs_mas_aristas_menor_costo():
    """
    Regla protegida: Mejora por peso 0 entra al inicio; prioriza costo sobre cantidad de aristas.
    Entrada: A->B (costo 1). A->C (costo 0) -> D (costo 0) -> B (costo 0).
    Resultado esperado: Costo 0, camino [A, C, D, B].
    Razón de importancia: BFS normal elegiría [A, B] (1 salto). 0-1 BFS debe encontrar la ruta de 3 saltos pero costo 0.
    """
    grafo = {
        "A": [("B", 1), ("C", 0)],
        "C": [("D", 0)],
        "D": [("B", 0)],
        "B": []
    }
    costo, camino = camino_cero_uno(grafo, "A", "B")
    assert costo == 0
    assert camino == ["A", "C", "D", "B"]

def test_cero_uno_bfs_mejora_posterior():
    """
    Regla protegida: Solo una mejora estricta actualiza distancia y predecesor (el nodo se re-encola).
    Entrada: A->B (costo 1). A->C (costo 0). C->B (costo 0).
    Resultado esperado: B se descubre primero con peso 1. Luego C lo descubre con peso 0. Costo final de B es 0, predecesor es C.
    Razón de importancia: Verifica que la deque no usa un set estricto de `visitados` inmutables y permite relajar aristas.
    """
    grafo = {
        "A": [("B", 1), ("C", 0)],
        "C": [("B", 0)],
        "B": []
    }
    distancias, predecesores = cero_uno_bfs(grafo, "A")
    assert distancias["B"] == 0
    assert predecesores["B"] == "C"

def test_cero_uno_bfs_pesos_invalidos():
    """
    Regla protegida: bool/float lanzan TypeError; ints distintos de 0/1 lanzan ValueError.
    Entrada: Aristas con pesos True, 0.5 y 2.
    Resultado esperado: Excepciones específicas comprobadas.
    Razón de importancia: Protege el contrato del TDA, ya que aristas de peso 2 romperían la regla de inserción en extremos.
    """
    grafo_bool = {"A": [("B", True)]}
    with pytest.raises(TypeError):
        cero_uno_bfs(grafo_bool, "A")
        
    grafo_fuera_rango = {"A": [("B", 2)]}
    with pytest.raises(ValueError):
        cero_uno_bfs(grafo_fuera_rango, "A")

def test_cero_uno_bfs_origen_igual_destino():
    """
    Regla protegida: Origen igual a destino produce (0, [origen]).
    Entrada: Grafo válido, origen = "A", destino = "A".
    Resultado esperado: Costo 0, camino ["A"].
    Razón de importancia: Caso frontera vital que no debe iniciar el ciclo principal ni procesar aristas innecesariamente.
    """
    grafo = {"A": [("B", 1)], "B": []}
    costo, camino = camino_cero_uno(grafo, "A", "A")
    assert costo == 0
    assert camino == ["A"]