import networkx as nx
import matplotlib.pyplot as plt

# 1. Definir el grafo base utilizado en la simulación
grafo_lista = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# 2. Inicializar el objeto de grafo no dirigido de NetworkX
G = nx.Graph()

# 3. Agregar las aristas desde la lista de adyacencia
for nodo, vecinos in grafo_lista.items():
    for vecino in vecinos:
        G.add_edge(nodo, vecino)

# 4. Configurar las propiedades estéticas del dibujo
plt.figure(figsize=(7, 5))

# Usamos un layout de resorte (spring) para separar los nodos simétricamente
pos = nx.spring_layout(G, seed=42) 

# Dibujar nodos, aristas y etiquetas
nx.draw_networkx_nodes(G, pos, node_color='#4A90E2', node_size=800, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=2, edge_color='#555555')
nx.draw_networkx_labels(G, pos, font_size=14, font_color='white', font_weight='bold')

plt.title("Estructura del Grafo de Ejemplo (Clase 10)", fontsize=14, fontweight='bold', pad=15)
plt.axis('off') # Ocultar los ejes cartesianos para una vista limpia

# 5. Guardar la imagen en alta calidad
plt.savefig('grafo.png', dpi=300, bbox_inches='tight')
plt.close()

print("¡Archivo 'grafo.png' generado y guardado con éxito en tu directorio actual!")