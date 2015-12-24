#!/bin/python
import directed_graph
import construct_graph




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

max_graph = construct_graph.initialize_graph(N)
min_graph = construct_graph.initialize_graph(N)
for i in range(len(A)):
    construct_graph.add_constraint(max_graph, A[i], B[i], C[i])
    construct_graph.add_constraint(min_graph, A[i], B[i], B[i] - A[i] + 1 - C[i])
max = construct_graph.get_max(max_graph, N)
min = N - construct_graph.get_max(min_graph, N)

print min,max
                   
