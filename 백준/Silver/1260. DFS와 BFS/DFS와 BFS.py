from collections import deque
N, M, V = map(int, input().split())
graph = {i:[] for i in range(1,N+1)}
for _ in range(M):
    front_node, back_node = map(int, input().split())
    graph[front_node].append(back_node)
    graph[back_node].append(front_node)
for key in graph:
    graph[key].sort()
    
def bfs(graph, start, path):
    visited = set([start])
    queue = deque([start])
    path.append(start)
    while queue:
        curr_node = queue.popleft()
        '''
        if curr_node == end:
            return path[curr_node]
        '''
        for nxt_node in graph[curr_node]:
            if nxt_node not in visited:
                visited.add(nxt_node)
                queue.append(nxt_node)
                path.append(nxt_node)
           
def dfs(graph, node, visited, path):
    visited.add(node)
    path.append(node)
    
    for nxt_node in graph[node]:
        if nxt_node not in visited:
            dfs(graph, nxt_node, visited, path)

bfs_path = []
dfs_visited = set()
dfs_path = []
bfs(graph, V, bfs_path)
dfs(graph, V, dfs_visited, dfs_path)
for i in dfs_path:
    print(i, end=' ')
print('')
for i in bfs_path:
    print(i, end=' ')