from collections import deque
def solution(n, edge):
    answer = 0
    '''
    1번에서 가장 멀리 떨어진 노드의 갯수 구하기
    n: number of node
    edge: 2 dim of matrix
    '''
    
    edge_dict = {}
    for ele in edge:
        
        if ele[0] not in edge_dict:
            edge_dict[ele[0]] = []
        if ele[1] not in edge_dict:
            edge_dict[ele[1]] = []
        
        edge_dict[ele[0]].append(ele[1])
        edge_dict[ele[1]].append(ele[0])
        
    def bfs(graph, start):
        queue = deque([start])
        visited = set([start])
        depth_dict = {start: 0}  # 시작 노드의 깊이는 0

        while queue:
            current = queue.popleft()

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    depth_dict[neighbor] = depth_dict[current] + 1  # 부모 깊이 + 1로 설정

        return depth_dict

    result = bfs(edge_dict, 1)
    answer_list = []
    for key in result:
        if result[key] == max(result.values()):
            answer_list.append(key)
    answer = len(answer_list)
    
    
    
    return answer