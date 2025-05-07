from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
def solution(edges):
    answer = []
    '''
    donut: n nodes, n edges
    stick: n nodes, n-1 edges
    eight: 2n+1 nodes, 2n+2 edges
    
    new_node -> connected with all graph
    '''
    
    out_graph_dict = defaultdict(list)
    in_graph_dict = defaultdict(list)
    graph_dict = defaultdict(list)
    
    for nodes in edges:
        start, end = nodes[0], nodes[1]
        out_graph_dict[start].append(end)
        in_graph_dict[end].append(start)
        graph_dict[start].append(end)
        graph_dict[end].append(start)
    
    # find new node, out: more than 2, in: 0
    # if number of out edges is more than 3, it is new node
    for key in out_graph_dict.keys():
        if len(out_graph_dict[key]) >= 3:
            new_node = key
            break
        elif len(out_graph_dict[key]) == 2:
            if key not in in_graph_dict.keys():
                new_node = key
                break
    
    def dfs(graph, curr, visited, path, num_edge):
        visited.add(curr)
        path.append(curr)

        num_edge[0] += len(graph[curr])
        for nxt in graph[curr]:
            if nxt not in visited:
                dfs(graph, nxt, visited, path, num_edge)
    
    visited = set([new_node])
    tot_graph = []
    for node in graph_dict[new_node]:
        path = []
        num_edge = [0]
        dfs(graph_dict, node, visited, path, num_edge)
        tot_graph.append([int((num_edge[0]-1)/2), path])
    
    answer = [new_node, 0, 0, 0]
    for ele in tot_graph:
        num_edge = ele[0]
        graph = ele[1]
        
        if num_edge == len(graph):
            answer[1] += 1
        elif num_edge == len(graph)-1:
            answer[2] += 1
        else:
            answer[3] += 1
    
    return answer