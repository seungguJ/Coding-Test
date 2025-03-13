from collections import deque
def solution(maps):
    answer = 0
    
    def bfs(graph, x, y):
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        end_x, end_y = len(graph)-1, len(graph[0])-1
        visited = set([(x,y)])
        queue = deque([(x,y, [(x,y)])]) # [(current x, current y, [(path x, path y)])]
        # [(path x, path y)] will be added recursivly
        
        while queue:
            x, y, path = queue.popleft()
            if x == end_x and y == end_y:
                return path
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx <= end_x and 0 <= ny <= end_y:
                    if (nx, ny) not in visited and graph[nx][ny] == 1:
                        visited.add((nx,ny))
                        queue.append((nx,ny, path+[(nx,ny)]))
    n,m=len(maps),len(maps[0])
    
    
    
    if maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0:
        return -1
        
    result = bfs(maps, 0,0)
    if result is None:
        return -1
    answer = len(result)
    
    return answer