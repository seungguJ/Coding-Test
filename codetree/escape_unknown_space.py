from collections import deque
import copy
'''
NxN 평면 어딘가에 M의 정육면체 존재
정육면체의 타임머신을 탈출구로 옮기기
정육면체는 출입구가 각각 하나
바닥에 F 개의 이상현상 존재 -> 매 vi의 배수 턴 마다 di방향으로 한 칸씩 확산
시작점에서 탈출구까지 이동하는 데 필요한 최소 턴 수, 탈출할 수 없으면 -1
우선순위: 타임머신 이동 < 이상현상 --> 이상현상 확산 후 타임머신 이동

0: 빈공간
1: 장애물
2: 타임머신의 위치 (시작점)
3: 시간의 벽 위치
4: 탈출구 (끝점)

- maze3D 타임머신 위치(2)에서 시작해서 출구까지 계산
- - bfs
- - 이상현상 확산
- 출구에서 나와서 (출구는 하나기에 시작점 동일) 탈출구까지 bfs
- - bfs
- - 시작점 찾아야함 # exit3D
'''

N, M, F = map(int, input().split())

maze2D = []
flag1 = True
for i in range(N):
    tmp = list(map(int, input().split()))
    if 3 in tmp and flag1:
        start3D = (i,tmp.index(3)) # 2D
        flag1 = False
    if 4 in tmp:
        endX, endY = i, tmp.index(4) # last exit
    maze2D.append(tmp)

for i in range(start3D[0]-1, start3D[0]+M+1):
    for j in range(start3D[1]-1, start3D[1]+M+1):
        if 0<= i < N and 0 <= j < N:
            if maze2D[i][j] == 0:
                exit3Din2D = (i,j) # 3D exit points in 2D maze
                relative_exit = (i-start3D[0]+1, j-start3D[1]+1) # 만약 relative_exit[0]이 0이라면 north에 출구 존재하며, relative_exit[1]-1번째 열에 존재
                break

# 3D maze
# 3D coordinate
# need to memorize start(2) and end point

maze3D = {i:[] for i in range(5)} # east, west, south, north, above
# east: ~west
# above: all
# south: ~north
# west: ~east
# north: ~south

for i in range(M): # east
    tmp = list(map(int, input().split()))
    a = 0 # east
    maze3D[a].append(tmp)
    if 2 in tmp:
        start=(a, i, tmp.index(2)) # location

for i in range(M): # west
    tmp = list(map(int, input().split()))
    a = 1 # west
    maze3D[a].append(tmp)
    if 2 in tmp:
        start=(a, i, tmp.index(2))

for i in range(M): # south
    tmp = list(map(int, input().split()))
    a = 2 # south
    maze3D[a].append(tmp)
    if 2 in tmp:
        start=(a, i, tmp.index(2))

for i in range(M): # north
    tmp = list(map(int, input().split()))
    a = 3
    maze3D[a].append(tmp)
    if 2 in tmp:
        start=(a, i, tmp.index(2))

for i in range(M): # above
    tmp = list(map(int, input().split()))
    a = 4
    maze3D[a].append(tmp)
    if 2 in tmp:
        start=(a, i, tmp.index(2))

anormal = []
for i in range(F):
    tmp = list(map(int, input().split())) # ri, ci, di, vi
    anormal.append(tmp)
    maze2D[tmp[0]][tmp[1]] = 1

def bfs3D(maze3D, start, end): # maze2D, count for diffusion and return maze2D and count
    visited = set([start])
    queue = deque([start])
    path = {start:[start]}

    M = len(maze3D[0])

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        curr_dir, currX, currY = queue.popleft()
        
        if (curr_dir, currX, currY) == end:
            return path[(curr_dir, currX, currY)]
        for i in range(4):
            nxtX, nxtY = currX+dx[i], currY+dy[i]
            nxt_dir = curr_dir
            if curr_dir == 0: # east
                if nxtY < 0: # toward south
                    nxt_dir = 2
                    nxtY = 2
                elif M-1 < nxtY: # toward north
                    nxt_dir = 3
                    nxtY = 0
                elif nxtX < 0: # toward above
                    nxt_dir = 4
                    nxtX = M-nxtY-1
                    nxtY = 2
            elif curr_dir == 1: # west
                if M-1 < nxtY: # toward south
                    nxt_dir = 2
                    nxtY = 0
                elif nxtY < 0: # toward north
                    nxt_dir = 3
                    nxtY = 2
                elif nxtX < 0: # toward above
                    nxt_dir = 4
                    nxtX = nxtY
                    nxtY = 0
            elif curr_dir == 2: # south
                if nxtY < 0: # toward west
                    nxt_dir = 1
                    nxtY = 2
                elif M-1 < nxtY: # toward east
                    nxt_dir = 0
                    nxtY = 0
                elif nxtX < 0: # toward above
                    nxt_dir = 4
                    nxtX = 2
            elif curr_dir == 3: # north
                if nxtY < 0: # toward east
                    nxt_dir = 0
                    nxtY = 2
                elif M-1 < nxtY: # toward west
                    nxt_dir = 1
                    nxtY = 0
                elif nxtX < 0: # toward above
                    nxt_dir = 4
                    nxtX = 0
                    nxtY = M-nxtY-1
            else: # above
                if nxtX < 0: # toward north
                    nxt_dir = 3
                    nxtX = 0
                    nxtY = M-nxtY-1
                elif M-1 < nxtX: # toward south
                    nxt_dir = 2
                    nxtX = 0
                elif nxtY < 0: # toward west
                    nxt_dir = 1
                    nxtY = nxtX
                    nxtX = 0
                elif M-1 < nxtY: # toward east
                    nxt_dir = 0
                    nxtY = M-nxtX-1
                    nxtX = 0
            if 0 <= nxtX < M and 0 <= nxtY < M:
                if (nxt_dir, nxtX, nxtY) not in visited:
                    if maze3D[nxt_dir][nxtX][nxtY] == 0:
                        queue.append((nxt_dir, nxtX, nxtY))
                        visited.add((nxt_dir, nxtX, nxtY))
                        path[(nxt_dir, nxtX, nxtY)] = path[(curr_dir, currX, currY)] + [(nxt_dir, nxtX, nxtY)]
    return -1

def bfs(maze, startX, startY, endX, endY, anormal, count):
    visited = set([(startX, startY)])
    queue = deque([(startX, startY)])
    path = {(startX, startY): [(startX, startY)]}
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        currX, currY = queue.popleft()

        if currX == endX and currY == endY:
            return path[(currX, currY)]
            # return count, maze

        for i in range(4):
            nxtX, nxtY = currX+dx[i], currY+dy[i]
            new_count = count + abs(startX-nxtX) + abs(startY-nxtY)
            maze, anormal = diffusion(maze, anormal, new_count)
            if (nxtX, nxtY) not in visited:
                if 0 <= nxtX < len(maze) and 0 <= nxtY < len(maze):
                    if maze[nxtX][nxtY] == 0 or maze[nxtX][nxtY] == 4:
                        visited.add((nxtX, nxtY))
                        queue.append((nxtX, nxtY))
                        path[(nxtX, nxtY)] = path[(currX, currY)] + [(nxtX, nxtY)]
    
    return -1

def dfs(maze, currX, currY, endX, endY, visited, path, total_path, anormal, count):
    visited.add((currX, currY))
    path.append((currX, currY))
    count+=1
    
    if currX == endX and currY == endY:
        total_path.append([count,path[:]])
    new_maze, anormal = diffusion(maze, anormal, count)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nxtX, nxtY = currX+dx[i], currY+dy[i]
        if (nxtX, nxtY) not in visited:
            if 0 <= nxtX < len(maze) and 0 <= nxtY < len(maze):
                if new_maze[nxtX][nxtY] == 0 or new_maze[nxtX][nxtY]==4:
                    dfs(new_maze, nxtX, nxtY, endX, endY, visited, path, total_path, anormal, count)
    count -=1
    path.pop()
    visited.remove((currX, currY))


def diffusion(maze, anormal, count):
    deleted = []
    for i in range(len(anormal)):
        r, c, d, v = anormal[i][0], anormal[i][1], anormal[i][2], anormal[i][3]
        remainder = count % v
        if remainder == 0: # time to diffuse
            step = count // v
            if d == 0: # east
                nxtr, nxtc = r, c+step
            elif d == 1: # west
                nxtr, nxtc = r, c-step
            elif d == 2: # south
                nxtr, nxtc = r+step, c
            else: # north
                nxtr, nxtc = r-step, c
            
            if 0 <= nxtr < len(maze) and 0 <= nxtc < len(maze): # ok to move
                if maze[nxtr][nxtc] != 0: # can not move
                    deleted.append(i) # index
                else:
                    maze[nxtr][nxtc] = 1
    
    tmp = 0
    for i in deleted:
        anormal.pop(i-tmp)
        tmp+=1

    return maze, anormal

# we need to find end point of 3D maze
if relative_exit[0] == 0: # exit is in north
    end3D = (3, M-1, M-relative_exit[1])
elif relative_exit[0] == M+1: # exit is in south
    end3D = (2, M-1, relative_exit[1]-1)
elif relative_exit[1] == 0: # exit is in west
    end3D = (1, M-1, relative_exit[0]-1)
else:
    end3D = (0, M-1, M-relative_exit[0])

result = bfs3D(maze3D, start, end3D) # len(result) 만큼 시간이 지남
if result == -1:
    print(-1)
else:
    count = len(result)
    for i in range(1,count):
        maze2D, anormal = diffusion(maze2D, anormal, i)
    ''' time over
    visited = set()
    path, total_path = [], []
    dfs(maze2D, exit3Din2D[0], exit3Din2D[1], endX, endY, visited, path, total_path, anormal, count)
    '''
    result = bfs(maze2D, exit3Din2D[0], exit3Din2D[1], endX, endY, anormal, count)
    if result == -1:
        print(-1)
    else:
        print(count+len(result)-1)