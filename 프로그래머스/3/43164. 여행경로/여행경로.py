from collections import defaultdict, Counter
def solution(tickets):
    answer = []
    '''
    방문하는 공항 경로 -> 모든 경로 탐색 -> DFS
    ICN에서 출발, 항공권 모두 사용, 알파벳 순서에따라 return
    
    1. 모두 순회 해야함
    2. 알파벳 순서
    
    dict <- dep:arr
    모두 순회 -> while tickets: 하나씩 소거
    '''
    
    tickets_counter = Counter((a,b) for a,b in tickets)

    tickets_dict = defaultdict(list)
    
    for ticket in tickets:
        dep, arr = ticket[0], ticket[1]
        tickets_dict[dep].append(arr)
        
    for key in tickets_dict.keys():
        tickets_dict[key].sort()
        
    
    def dfs(graph, node, tickets, visited, path, answer):
        path.append(node) # path 저장
        if len(visited) == len(tickets):
            answer.extend(path)
            return True
        
        for nxt_node in graph[node]:
            if tickets_counter[(node, nxt_node)] != 0:
                visited.append([node, nxt_node])
                tickets_counter[(node,nxt_node)] -= 1
                if dfs(graph, nxt_node, tickets, visited, path, answer):
                    return True
                visited.pop() # 여기까지 왔다는 것은 앞의 재귀가 다 끝났다는 것 -> 다음 경로 탐색
                tickets_counter[(node,nxt_node)] += 1
        
        path.pop() # 잘못찾아왔으니 경로 수정
            
    
    visited, path = [], []
    dfs(tickets_dict, "ICN", tickets, visited, path, answer)
    print(answer)
    
        
    return answer