from collections import deque
'''
숲 -> 북쪽에서만 출입 가능
K명 의 정령
골렘: 십자 모양 -> 5칸 차지
정령은 골렘에서 내릴때 정해진 출구에서 내려야함, 탈땐 상관 X
i번째의 솔렘은 중앙이 ci열에서 내려옴, 출구: di
이동 -> 앞 3칸이 모두 비어있어야함
1. 아래
2. 왼쪽 (출구가 반시계로 이동) 아래
3. 오른쪽 (출구가 시계로 이동) 아래
다른 골렘과 인접하다면 출구를 통해 다른 골렘으로 이동 가능
만약 정령이 숲 바깥에 있고 움직일 수 없다면 숲을 비움, 다음 정령 입장

R,C: 숲의 크기
K: 정령 수
K개의 골렘 출발 열: c_i, 골렘의 출구 방향 정보: d_i (0,1,2,3 -> 북동남서)

return: 정령들이 최종적으로 위치한 행의 총 합

forest: 숲 -> 0: 비어있음, 1.i: 골렘이 차지함, i: 골렘이 차지한 부분의 출구
forest안에서 값이 같거나, 1일 때 움직일 수 있다.

bfs -> forest 골렘 채우기
dfs -> 정령 최적 루트 찾기

'''
R, C, K = map(int, input().split())

forest = [[0 for _ in range(C)] for _ in range(R)]

answer = 0

def bfs(forest, startX, startY, exit):
    visited = set([(startX, startY, exit)])
    queue = deque([(startX, startY, exit)])

    dx = [(1,0, 0), (0, -1, -1), (0, 1, 1)]

    while queue:
        currX, currY, curr_Exit = queue.popleft() # location of soul

        if currX == -2: # outside of forest
            # if go down
            if forest[currX+2][currY] == 0:
                nxtX, nxtY, nxt_Exit = currX+1, currY, curr_Exit # go down
                if (nxtX, nxtY, nxt_Exit) not in visited:
                    visited.add((nxtX, nxtY, nxt_Exit))
                    queue.append((nxtX, nxtY, nxt_Exit))
            # if go left and down
            elif forest[currX+2][currY-1] == 0 and 1 < currY:
                nxtX, nxtY, nxt_Exit = currX+1, currY-1, curr_Exit-1
                nxt_Exit = nxt_Exit % 4
                if (nxtX, nxtY, nxt_Exit) not in visited:
                    visited.add((nxtX, nxtY, nxt_Exit))
                    queue.append((nxtX, nxtY, nxt_Exit))
            # if go right and down
            elif forest[currX+2][currY+1] == 0 and currY < len(forest[0])-1:
                nxtX, nxtY, nxt_Exit = currX+1, currY+1, curr_Exit+1
                nxt_Exit = nxt_Exit % 4
                if (nxtX, nxtY, nxt_Exit) not in visited:
                    visited.add((nxtX, nxtY, nxt_Exit))
                    queue.append((nxtX, nxtY, nxt_Exit))
        
        if currX == -1:
            # if go down
            if forest[currX+1][currY-1] == 0 and forest[currX+2][currY] == 0 and forest[currX+1][currY+1] == 0:
                nxtX, nxtY, nxt_Exit = currX+1, currY, curr_Exit # go down
                if (nxtX, nxtY, nxt_Exit) not in visited:
                    visited.add((nxtX, nxtY, nxt_Exit))
                    queue.append((nxtX, nxtY, nxt_Exit))
            # if go left and go down
            elif 1 < currY and forest[currX+2][currY-1] == 0 and forest[currX+1][currY-2] == 0 and forest[currX+1][currY] == 0:
                nxtX, nxtY, nxt_Exit = currX+1, currY-1, curr_Exit-1
                nxt_Exit = nxt_Exit % 4
                if (nxtX, nxtY, nxt_Exit) not in visited:
                    visited.add((nxtX, nxtY, nxt_Exit))
                    queue.append((nxtX, nxtY, nxt_Exit))
            # if go right and go down
            elif currY < len(forest[0])-2 and forest[currX+2][currY+1] == 0 and forest[currX+1][currY+2] == 0 and forest[currX+1][currY] == 0:
                nxtX, nxtY, nxt_Exit = currX+1, currY+1, curr_Exit+1
                nxt_Exit = nxt_Exit % 4
                if (nxtX, nxtY, nxt_Exit) not in visited:
                    visited.add((nxtX, nxtY, nxt_Exit))
                    queue.append((nxtX, nxtY, nxt_Exit))

        if currX == 0:
            # if go down
            if forest[currX+1][currY-1] == 0 and forest[currX+2][currY] == 0 and forest[currX+1][currY+1] == 0:
                nxtX, nxtY, nxt_Exit = currX+1, currY, curr_Exit # go down
                if (nxtX, nxtY, nxt_Exit) not in visited:
                    visited.add((nxtX, nxtY, nxt_Exit))
                    queue.append((nxtX, nxtY, nxt_Exit))
            # if go left and go down
            elif 1 < currY and forest[currX][currY-2] == 0 and forest[currX+1][currY-1] == 0 and \
            forest[currX+2][currY-1] == 0 and forest[currX+1][currY-2] == 0 and forest[currX+1][currY] == 0:
                nxtX, nxtY, nxt_Exit = currX+1, currY-1, curr_Exit-1
                nxt_Exit = nxt_Exit % 4
                if (nxtX, nxtY, nxt_Exit) not in visited:
                    visited.add((nxtX, nxtY, nxt_Exit))
                    queue.append((nxtX, nxtY, nxt_Exit))
            # if go right and go down
            elif currY < len(forest[0])-2 and forest[currX][currY+2] == 0 and forest[currX+1][currY+1] == 0 and \
            forest[currX+2][currY+1] == 0 and forest[currX+1][currY+2] == 0 and forest[currX+1][currY] == 0:
                nxtX, nxtY, nxt_Exit = currX+1, currY+1, curr_Exit+1
                nxt_Exit = nxt_Exit % 4
                if (nxtX, nxtY, nxt_Exit) not in visited:
                    visited.add((nxtX, nxtY, nxt_Exit))
                    queue.append((nxtX, nxtY, nxt_Exit))

        else:
            
            if currX < len(forest)-2:
                # if go down
                if forest[currX+1][currY-1] == 0 and forest[currX+2][currY] == 0 and forest[currX+1][currY+1] == 0:
                    nxtX, nxtY, nxt_Exit = currX+1, currY, curr_Exit # go down
                    if (nxtX, nxtY, nxt_Exit) not in visited:
                        visited.add((nxtX, nxtY, nxt_Exit))
                        queue.append((nxtX, nxtY, nxt_Exit))
                # if go left and go down
                elif 1 < currY and forest[currX][currY-2] == 0 and forest[currX+1][currY-1] == 0 and forest[currX-1][currY-1] == 0 and \
                forest[currX+2][currY-1] == 0 and forest[currX+1][currY-2] == 0 and forest[currX+1][currY] == 0:
                    nxtX, nxtY, nxt_Exit = currX+1, currY-1, curr_Exit-1
                    nxt_Exit = nxt_Exit % 4
                    if (nxtX, nxtY, nxt_Exit) not in visited:
                        visited.add((nxtX, nxtY, nxt_Exit))
                        queue.append((nxtX, nxtY, nxt_Exit))
                # if go right and go down
                elif currY < len(forest[0])-2 and forest[currX][currY+2] == 0 and forest[currX+1][currY+1] == 0 and forest[currX-1][currY+1] == 0 and \
                forest[currX+2][currY+1] == 0 and forest[currX+1][currY+2] == 0 and forest[currX+1][currY] == 0:
                    nxtX, nxtY, nxt_Exit = currX+1, currY+1, curr_Exit+1
                    nxt_Exit = nxt_Exit % 4
                    if (nxtX, nxtY, nxt_Exit) not in visited:
                        visited.add((nxtX, nxtY, nxt_Exit))
                        queue.append((nxtX, nxtY, nxt_Exit))
                
                else:
                    continue

    return currX, currY, curr_Exit


def dfs(forest, currX, currY, visited, path, total_path, max_val):
    visited.add((currX, currY))
    path.append((currX, currY))
    if currX == len(forest)-1:
        total_path.append(path[:])
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    curr_val = forest[currX][currY]
    for i in range(4):
        nxtX, nxtY = currX+dx[i], currY+dy[i]
        if (nxtX, nxtY) not in visited:
            if 0 <= nxtX < len(forest) and 0 <= nxtY < len(forest[0]):
                nxt_val = forest[nxtX][nxtY]
                if curr_val % 1 == 0 and nxt_val != 0: # from exit to next golem
                    if max_val[0] < nxtX + 1:
                        max_val[0] = nxtX+1
                    dfs(forest, nxtX, nxtY, visited, path, total_path, max_val)
                elif curr_val == nxt_val: # move in same golem
                    if max_val[0] < nxtX + 1:
                        max_val[0] = nxtX+1
                    dfs(forest, nxtX, nxtY, visited, path, total_path, max_val)
                elif int(round(curr_val * 1000 % 1000)) == nxt_val and nxt_val != 0: # from same golem to same golem exit
                    if max_val[0] < nxtX + 1:
                        max_val[0] = nxtX+1
                    dfs(forest, nxtX, nxtY, visited, path, total_path, max_val)
    
    visited.remove((currX, currY))
    path.pop()

def bfs2(forest, startX, startY):

    visited = set([(startX, startY)])
    max_row = -1
    queue = deque([(startX, startY)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        currX, currY = queue.popleft()
        curr_val = forest[currX][currY]
        if currX == len(forest)-1:
            max_row = len(forest)
            return max_row
        if max_row < currX+1:
            max_row = currX + 1
        
        for i in range(4):
            nxtX, nxtY = currX + dx[i], currY+dy[i]
            if 0 <= nxtX < len(forest) and 0 <= nxtY < len(forest[0]):
                if (nxtX, nxtY) not in visited:
                    nxt_val = forest[nxtX][nxtY]
                    if curr_val % 1 == 0 and nxt_val != 0: # from exit to next  golem
                        visited.add((nxtX, nxtY))
                        queue.append((nxtX, nxtY))
                    elif curr_val == nxt_val: # move in same golem
                        visited.add((nxtX, nxtY))
                        queue.append((nxtX, nxtY))
                    elif int(round(curr_val * 1001 % 1001)) == nxt_val and nxt_val != 0: # from same golem to same golem exit
                        visited.add((nxtX, nxtY))
                        queue.append((nxtX, nxtY))
    return max_row
        

for i in range(1, K+1):
    currY, exit = map(int, input().split())
    currY -= 1
    currX = -2
    X, Y, exit = bfs(forest, currX, currY, exit)
    # print(X,Y,exit)

    if X <= 0:
        forest = [[0 for _ in range(C)] for _ in range(R)]
    
    else:
        curr_golem = 1 + i/1001
        forest[X][Y] = curr_golem
        if X < 1:
            pass
        else:
            forest[X-1][Y] = curr_golem
        forest[X][Y+1] = curr_golem
        forest[X+1][Y] = curr_golem
        if Y < 1:
            pass
        else:
            forest[X][Y-1] = curr_golem

        if exit == 0:
            if X < 1:
                pass
            else:
                forest[X-1][Y] = i
        elif exit == 1:
            forest[X][Y+1] = i
        elif exit == 2:
            forest[X+1][Y] = i
        else:
            if Y < 1:
                pass
            else:
                forest[X][Y-1] = i

        # visited, max_val = set(), [-1]
        # path, total_path = [], []
        # dfs(forest, X, Y, visited, path, total_path, max_val)
        # print(max_val[0])
        # answer += max_val[0]
        max_row = bfs2(forest, X, Y)
        # print(max_row)
        answer += max_row
        
print(answer)