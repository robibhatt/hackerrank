import construct_graph
import directed_graph

def test_initialize():
    graph = construct_graph.initialize_graph(100)
    distances = graph.bellman_ford(0)
    for v in distances.keys():
        assert v == distances[v]
    print "passed test_initialize"

def test_add_edge_smart():
    graph = construct_graph.initialize_graph(100)
    construct_graph.add_edge_smart(graph, (30, 31, -1))
    construct_graph.add_edge_smart(graph, (30, 32, 1))
    construct_graph.add_edge_smart(graph, (30, 31, 2))
    assert graph.get_edge_weight(30, 31) == -1
    assert graph.get_edge_weight(30, 32) == 1
    print "passed test_add_edge_smart"

test_initialize()
test_add_edge_smart()
