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
    
