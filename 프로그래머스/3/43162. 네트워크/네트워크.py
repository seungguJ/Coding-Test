def solution(n, computers):
    '''
    해당 node와 연결된 node들 list만들기
    만약 여러 개의 list(graph)와 연결된 node라면, 여러 list(graph) 병합
    만약 node가 list(graph)안에 있으면 연결된 node들을 해당 list(graph)에 추가
    만약 list(graph)에 없다면 새로 list(graph) 추가
    
    symmetric matrix니까, upper triangle만 확인
    '''
    answer = 0
    graph_list = []
    for i in range(len(computers)): # i: node number
        count = [] # 현재 노드가 몇 번째의 그래프에 속해있는지
        for graph_idx in range(len(graph_list)):
            if i in graph_list[graph_idx]: # 몇 번째 그래프에 속해있는지
                count.append(graph_idx)
            else:
                pass
        new_graph = set()
        for j in range(len(computers[i])): # j: connection info with node i
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
            
    return answer