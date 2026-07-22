from collections import deque

class NormalizadorGrafo:
    def procesar(self, grafo: dict) -> dict:
        if not isinstance(grafo, dict):
            raise TypeError("El grafo debe ser una estructura de mapeo.")
            
        resultado = {}
        
        # Guarda primero los nombres de las tareas principales
        for origen in grafo:
            if not isinstance(origen, str):
                raise TypeError("Todas las claves del grafo deben ser cadenas de texto.")
            if origen not in resultado:
                resultado[origen] = []
                
        # Revisa las conexiones de cada tarea evitando duplicados
        for origen, vecinos in grafo.items():
            if isinstance(vecinos, str) or not hasattr(vecinos, "__iter__"):
                raise TypeError("Los vecinos deben ser una secuencia (lista o tupla) de cadenas.")
                
            for destino in vecinos:
                if not isinstance(destino, str):
                    raise TypeError("Cada vecino debe ser una cadena de texto.")
                
                # Si una tarea destino no estaba registrada, la agrega a la lista
                if destino not in resultado:
                    resultado[destino] = []
                    
                # Agrega la tarea destino solo si no se había anotado ya
                if destino not in resultado[origen]:
                    resultado[origen].append(destino)
                    
        return resultado


class CalculadorGrados:
    def __init__(self):
        self.normalizador = NormalizadorGrafo()

    def calcular(self, grafo: dict) -> dict:
        normalizado = self.normalizador.procesar(grafo)
        grados = {nodo: 0 for nodo in normalizado}
        
        # Cuenta cuántas tareas dependen directamente de otras
        for vecinos in normalizado.values():
            for destino in vecinos:
                grados[destino] += 1
                
        return grados


class OrdenadorTopologico:
    def __init__(self):
        self.normalizador = NormalizadorGrafo()
        self.calculador = CalculadorGrados()

    def ordenar(self, grafo: dict) -> list | None:
        normalizado = self.normalizador.procesar(grafo)
        grados = self.calculador.calcular(normalizado)
        
        # Separa las tareas que no tienen ningún requisito previo
        disponibles = deque(nodo for nodo in normalizado if grados[nodo] == 0)
        orden = []
        
        while disponibles:
            actual = disponibles.popleft()
            orden.append(actual)
            
            # Le quita un requisito pendiente a las tareas siguientes
            for vecino in normalizado[actual]:
                grados[vecino] -= 1
                # Si la tarea se quedó sin requisitos, ya se puede realizar
                if grados[vecino] == 0:
                    disponibles.append(vecino)
                    
        # Si no se acomodaron todas las tareas, hay una traba circular
        if len(orden) != len(normalizado):
            return None
            
        return orden


class ValidadorOrden:
    def __init__(self):
        self.normalizador = NormalizadorGrafo()

    def verificar(self, grafo: dict, orden: list | None) -> bool:
        if orden is None:
            return False
            
        normalizado = self.normalizador.procesar(grafo)
        
        # Revisa que estén exactamente las mismas tareas y sin repetir
        if len(orden) != len(normalizado) or len(set(orden)) != len(orden):
            return False
            
        posiciones = {nodo: indice for indice, nodo in enumerate(orden)}
        
        for nodo in posiciones:
            if nodo not in normalizado:
                return False
                
        # Comprueba que ninguna tarea se haga antes que sus requisitos
        for origen, vecinos in normalizado.items():
            for destino in vecinos:
                if posiciones[origen] >= posiciones[destino]:
                    return False
                    
        return True


class OrdenadorCursos:
    def ordenar(self, numero_cursos: int, prerrequisitos: list) -> list | None:
        if type(numero_cursos) is not int or numero_cursos < 0:
            if type(numero_cursos) is int and numero_cursos < 0:
                raise ValueError("La cantidad de cursos debe ser un entero no negativo.")
            raise TypeError("La cantidad de cursos debe ser un entero no negativo.")
            
        if isinstance(prerrequisitos, str) or not hasattr(prerrequisitos, "__iter__"):
            raise TypeError("Los prerrequisitos deben ser una secuencia estructurada.")
            
        # Crea la lista de materias usando números para identificarlas
        grafo = {i: [] for i in range(numero_cursos)}
        
        for par in prerrequisitos:
            if isinstance(par, str) or not hasattr(par, "__iter__"):
                raise TypeError("Cada par de dependencias debe ser una lista o tupla.")
                
            if len(par) != 2:
                raise ValueError("Cada par de dependencias debe contener exactamente dos elementos.")
            
            u, v = par[0], par[1]
            if type(u) is not int or type(v) is not int:
                raise TypeError("Los identificadores de los cursos deben ser valores enteros.")
                
            if not (0 <= u < numero_cursos) or not (0 <= v < numero_cursos):
                raise IndexError("Los índices de los cursos se encuentran fuera del rango permitido.")
                
            if v not in grafo[u]:
                grafo[u].append(v)
                
        # Cuenta cuántos candados tiene cada materia para poder cursarse
        grados = {i: 0 for i in range(numero_cursos)}
        for vecinos in grafo.values():
            for destino in vecinos:
                grados[destino] += 1
                
        # Empieza con los cursos libres de candados
        disponibles = deque(i for i in range(numero_cursos) if grados[i] == 0)
        orden = []
        
        while disponibles:
            actual = disponibles.popleft()
            orden.append(actual)
            for vecino in grafo[actual]:
                grados[vecino] -= 1
                if grados[vecino] == 0:
                    disponibles.append(vecino)
                    
        if len(orden) != numero_cursos:
            return None
            
        return orden


class VerificadorCursos:
    def __init__(self):
        self.ordenador_cursos = OrdenadorCursos()

    def verificar(self, numero_cursos: int, prerrequisitos: list) -> bool:
        # Reutiliza el ordenamiento para saber si es posible terminar las materias
        return self.ordenador_cursos.ordenar(numero_cursos, prerrequisitos) is not None


# Enlaces de salida corregidos con los nombres exactos de los métodos
normalizar_grafo_dirigido = NormalizadorGrafo().procesar
grados_entrada = CalculadorGrados().calcular
orden_topologico = OrdenadorTopologico().ordenar
es_orden_topologico = ValidadorOrden().verificar
ordenar_cursos = OrdenadorCursos().ordenar
puede_completar_cursos = VerificadorCursos().verificar