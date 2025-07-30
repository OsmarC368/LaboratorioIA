import networkx as nx
import matplotlib.pyplot as plt


def count(path, graph):
    sum = 0
    for i in range(len(path)-1):
        sum += graph[path[i]][path[i+1]]
    return sum

def graph(graph, route):
    G = nx.Graph()
    nodes = [x for x in graph]
    G.add_nodes_from(nodes)

    for x in graph:
        for i in graph[x]:
            G.add_edge(x, i, weight=graph[x][i])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=800, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    camino_destacado = []
    for i in range(len(route)-1):
        camino_destacado.append((route[i], route[i+1]))

    nx.draw_networkx_edges(G, pos, edgelist=camino_destacado, width=4, edge_color='red', arrows=True, arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color='orange')

# Mostrar el grafo
    plt.show()



   