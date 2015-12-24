class Directed_Graph:

    inward = 0
    outward = 1

    def __init__(self):
        self.graph_dict = {}

    def num_vertices(self):
        return len(self.graph_dict.keys())

        
    def add_vertex(self, vertex):
        if vertex in self.graph_dict.keys():
            raise ValueError('trying to add same vertex multiple times')
        out_edges = {}
        in_edges = {}
        self.graph_dict[vertex] = (in_edges, out_edges)


    def add_edge(self, edge):
        (from_vertex, to_vertex, weight) = edge
        self.graph_dict[from_vertex][self.outward][to_vertex] = weight
        self.graph_dict[to_vertex][self.inward][from_vertex] = weight
        

    def list_vertices(self):
        return self.graph_dict.keys()
    

    def list_edges(self):
        edges = []
        for v in self.graph_dict.keys():
            edges += [(v, x, self.graph_dict[v][self.outward][x]) for x in self.graph_dict[v][self.outward].keys()]
        return edges

    def num_edges(self):
        number = 0
        for v in self.graph_dict.keys():
            number += len(self.graph_dict[v][self.outward].keys())
        return number

    def bellman_ford(self, source):
        distances = {}
        distances[source] = 0
        for i in range(self.num_vertices() - 1):
            for (u,v,w) in self.list_edges():
                if u in distances.keys():
                    if v in distances.keys():
                        if distances[v] > distances[u] + w:
                            distances[v] = distances[u] + w
                    else:
                        distances[v] = distances[u] + w
        return distances

    def delete_edge(self, (u,v,w)):
        del (self.graph_dict[u][self.outward][v])
        del (self.graph_dict[v][self.inward][u])

    def delete_vertex(self, u):
        for v in self.graph_dict[u][self.outward].keys():
            del (self.graph_dict[v][self.inward][u])
        for v in self.graph_dict[u][self.inward].keys():
            del (self.graph_dict[v][self.outward][u])
        del self.graph_dict[u]
        
    def get_outer_edges(self, u):
        return self.graph_dict[u][self.outward]

    def get_inner_edges(self, u):
        return self.graph_dict[u][self.inward]

    def get_edge_weight(self, u,v):
        if v in self.graph_dict[u][self.outward].keys():
            return self.graph_dict[u][self.outward][v]
        else:
            return None


def initialize_graph(N):
    graph = Directed_Graph()
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



# code snippet for illustrating input/output

inp = raw_input()
N, M = [int(x) for x in inp.split(' ')]

A = []
B = []
C = []

for i in range(0, M):

    numbers = raw_input()
    a, b, c = [int(x) for x in numbers.split(' ')]
    A.append(a)
    B.append(b)
    C.append(c)

max_graph = initialize_graph(N)
min_graph = initialize_graph(N)
for i in range(len(A)):
    add_constraint(max_graph, A[i], B[i], C[i])
    add_constraint(min_graph, A[i], B[i], B[i] - A[i] + 1 - C[i])
max = get_max(max_graph, N)
min = N - get_max(min_graph, N)

print min,max
                   
