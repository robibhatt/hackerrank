import directed_graph

def initialize_graph(N):
    graph = directed_graph.Directed_Graph()
    for i in range(N+1):
        graph.add_vertex(i)
    for j in range(N):
        graph.add_edge((j, j+1, 1))
        graph.add_edge((j+1, j, 0))
    return graph

def add_edge_smart(graph, (u,v,w)):
    if graph.get_edge_weight(u, v) == None:
        graph.add_edge((u,v,w))
    else:
        if graph.get_edge_weight(u,v) > w:
            graph.add_edge((u,v,w))

def add_constraint(graph, A, B, C):
    add_edge_smart(graph, (A-1, B, C))
    add_edge_smart(graph, (B, A-1, -C))

def get_max(graph, N):
    return graph.bellman_ford(0)[N]
