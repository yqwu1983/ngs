#!/usr/bin/python
import os

def read_from_file(file_path):
    with open(file_path, 'r') as f:
        first = True
        adj_list = []
        for s in f:
            if first:
                n_points = int(s)
                first = False
            else:
                edge = (int(s.rsplit()[0]), int(s.rsplit()[1]))
                adj_list.append(edge)
        f.closed
    return n_points, adj_list

def count_nodes(n_points, adj_list):
    connected_graphs = []
    first = True

    for edge in adj_list:
        if first:
            connected_graphs.append(list(edge))
            first = False
        else:
            connecting_nodes = []
            for vertex in edge:
                for graph in connected_graphs:
                    if vertex in graph:
                        connecting_node = {}
                        graph_index = connected_graphs.index(graph)
                        connecting_node['vertex'] = vertex
                        connecting_node['vertex_index'] = edge.index(vertex)
                        connecting_node['graph_index'] = graph_index
                        connecting_nodes.append(connecting_node)

            if len(connecting_nodes) == 0:
                connected_graphs.append(list(edge))

            elif len(connecting_nodes) == 1:
                connecting_node = connecting_nodes[0]
                new_vertex_index = connecting_node['vertex_index']-1
                new_vertex = edge[new_vertex_index]
                graph_index = connecting_node['graph_index']
                connected_graphs[graph_index].append(new_vertex)

            elif len(connecting_nodes) == 2:
                new_connected_graphs = []
                for i in range(len(connected_graphs)):
                    is_uniting = False
                    for connecting_node in connecting_nodes:
                        if connecting_node['graph_index'] == i:
                            is_uniting = True
                    if not is_uniting:
                        new_connected_graphs.append(connected_graphs[i])

                first_graph_index = connecting_nodes[0]['graph_index']
                first_graph = connected_graphs[first_graph_index]
                second_graph_index = connecting_nodes[1]['graph_index']
                second_graph = connected_graphs[second_graph_index]
                new_united_graph = first_graph + second_graph
                new_connected_graphs.append(new_united_graph)
                connected_graphs = new_connected_graphs

            else:
                print "Error!"
                os.exit(1)

    free_points = []

    for point in range(1, n_points + 1):
        is_free_point = True
        for graph in connected_graphs:
            if point in graph:
                is_free_point = False
        if is_free_point:
            free_points.append(point)

    result = len(connected_graphs) + len(free_points) - 1
    return result

def tree(file_path):
    n_points, adj_list = read_from_file(file_path)
    result = count_nodes(n_points, adj_list)
    return result

file_path = '/home/anna/bioinformatics/ngs/rosalind/data/rosalind_tree.txt'

print tree(file_path)