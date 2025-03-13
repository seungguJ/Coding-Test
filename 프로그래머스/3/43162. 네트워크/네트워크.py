def solution(n, computers):
    answer = 0
    '''
    해당 node와 연결된 node들 list만들기
    만약 여러 개의 list(graph)와 연결된 node라면, 여러 list(graph) 병합
    만약 node가 list(graph)안에 있으면 연결된 node들을 해당 list(graph)에 추가
    만약 list(graph)에 없다면 새로 list(graph) 추가
    
    symmetric matrix니까, upper triangle만 확인
    '''
    '''
    graph_list = []
    for i in range(len(computers)): # i: node number
        count = [] # 현재 노드가 몇 번째의 그래프에 속해있는지
        for graph_idx in range(len(graph_list)):
            if i in graph_list[graph_idx]: # 몇 번째 그래프에 속해있는지
                count.append(graph_idx)
            else:
                pass
        new_graph = set()
        for j in range(i+1, len(computers[i])): # j: connection info with node i
            if computers[i][j] == 1:
                new_graph.add(j)
        if len(count) == 0:
            graph_list.append(new_graph)
        elif len(count) == 1:
            graph_list[count[0]] = graph_list[count[0]].union(new_graph)
        else:
            tmp = set()
            removed=[]
            for count_idx in count:
                tmp = tmp.union(graph_list[count_idx])
                removed.append(graph_list[count_idx])
            for removed_graph in removed:
                graph_list.remove(removed_graph)
            graph_list.append(tmp.union(new_graph))
    answer = len(graph_list)
    '''
    
    # DFS sol
    '''
    1. 모든 node 탐색 -> for i in range(n)
    2. 현재 노드의 연결 상태 탐색 -> 방문했다면 visited = True (1 번에서 돌지 않기 위함)
    3. 2번과 연결된 노드에서 dfs 호출 -> 방문할 때 마다 visited = True
    '''
    '''
    1번 노드 확인 -> 2 번이랑 연결되어있네 2 번은 누구랑 연결되어있지... 반복
    '''
    '''
    def dfs(n, computers, curr_com, visited):
        visited[curr_com] = True # 방문
        for i in range(n): # 현재 노드와 연결상태 확인
            # 현재 노드와 연결되어있어야하며, 방문한 적 없고,자기자신이 아니어야함
            if computers[curr_com][i] == 1 and visited[i] == False and i != curr_com:
                dfs(n, computers, i, visited) # 3번
    
    visited = [False for _ in range(n)]
    
    for i in range(n): # 1 번
        if visited[i] == False:
            dfs(n, computers, i, visited)
            answer+=1
    '''
    
    def dfs(graph,n, node, visited, path):
        path.append(node)
        visited.add(node)
        for i in range(n):
            if graph[node][i] == 1 and i not in visited and i != node:
                dfs(graph, n, i, visited, path)
                # visited.pop()
        path.pop()
        
    
    tot_path = []
    for i in range(n):
        visited, path = set(), []
        dfs(computers, n, i, visited, path)
        if visited not in tot_path:
            tot_path.append(visited)
    print(tot_path)
    
    answer = len(tot_path)
    
    return answer