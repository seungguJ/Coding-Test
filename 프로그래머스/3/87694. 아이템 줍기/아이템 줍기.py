from collections import deque, defaultdict
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    '''
    테두리 추출 -> zeros mat -> 테두리 1, 내부 2 -> 테두리가 내부를 만나면 pass
    '''
    
    matrix = [[0 for _ in range(51)] for _ in range(51)]
    intersection = set() # 교차점 저장해서 기존 방향대로 못 움직이도록 설정
    rec_dict = defaultdict(list) # 현재 사각형 정보 저장
    for idx in range(len(rectangle)):
        l_bot = (rectangle[idx][0], rectangle[idx][1])
        r_top = (rectangle[idx][2], rectangle[idx][3])
        
        for row in range(l_bot[1], r_top[1]+1): # row -> y coordinate
            for col in range(l_bot[0], r_top[0]+1): # col -> x coordinate
                if row == l_bot[1] or row == r_top[1] or col == l_bot[0] or col == r_top[0]:
                    rec_dict[(col, row)].append(idx)
                    if matrix[row][col] == 1:
                        intersection.add((col, row))
                    if matrix[row][col] != 2: # not interior
                        matrix[row][col] = 1
                else:
                    matrix[row][col] = 2 # interior
    
    def is_penetrate(rec, curr_X, curr_Y, nxt_X, nxt_Y): # 관통 여부
        # 좌표 끝에서 움직임이 일어나야함
        if curr_X == rec[0] or curr_X == rec[2]: # x 좌표가 끝에 있을 때 -> Y 좌표만 움직일 수 있음
            if curr_Y != rec[1] and curr_Y != rec[3]: # 꼭짓점 제외
                if curr_X != nxt_X: # 다르면 관통한다
                    return True
        elif curr_Y == rec[1] or curr_Y == rec[3]: # y 좌표가 끝에 있을 때 -> X 좌표만 움직일 수 있음
            if curr_X != rec[0] and curr_X != rec[2]: # 꼭짓점 제외
                if curr_Y != nxt_Y:
                    return True
        return False
        
    
    def bfs(rectangle, graph, start_X, start_Y, end_X, end_Y):
        queue = deque([(start_X, start_Y, 0)]) # 0: direction -> 0:start, 1: right, left, 2: up, down
        visited = set([(start_X, start_Y)])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        path = {}
        path[(start_X, start_Y)] = [(start_X, start_Y)]
        
        while queue:
            curr_X, curr_Y, curr_dir = queue.popleft()
            curr_rec_idx = rec_dict[(curr_X, curr_Y)]
            
            is_intersection = (curr_X, curr_Y) in intersection
            
            if curr_X == end_X and curr_Y == end_Y:
                return path[(end_X, end_Y)]
            
            for i in range(4):
                nxt_X = curr_X+dx[i]
                nxt_Y = curr_Y+dy[i]
                nxt_rec_idx = rec_dict[(nxt_X, nxt_Y)]
                if abs(dx[i]) == 1:
                    nxt_dir = 1
                else:
                    nxt_dir = 2
                if 0 < nxt_Y < len(graph) and 0 < nxt_X < len(graph[0]):
                    if (nxt_X, nxt_Y) not in visited:
                        if is_intersection:
                            if curr_dir != nxt_dir:
                                count = 0
                                for nxt_idx in nxt_rec_idx:
                                    if is_penetrate(rectangle[nxt_idx], curr_X, curr_Y, nxt_X, nxt_Y):
                                        count =1
                                if count != 0:
                                    continue
                                for curr_idx in curr_rec_idx:
                                    if curr_idx in nxt_rec_idx:
                                        if graph[nxt_Y][nxt_X] == 1:
                                            queue.append((nxt_X, nxt_Y, nxt_dir))
                                            visited.add((nxt_X, nxt_Y))
                                            path[(nxt_X, nxt_Y)] = path[(curr_X, curr_Y)] + [(nxt_X, nxt_Y)]
                                            break
                        else:
                            count = 0
                            for nxt_idx in nxt_rec_idx:
                                if is_penetrate(rectangle[nxt_idx], curr_X, curr_Y, nxt_X, nxt_Y):
                                    count =1
                            if count != 0:
                                continue
                            for curr_idx in curr_rec_idx:
                                if curr_idx in nxt_rec_idx:
                                    if graph[nxt_Y][nxt_X] == 1:
                                        queue.append((nxt_X, nxt_Y, nxt_dir))
                                        visited.add((nxt_X, nxt_Y))
                                        path[(nxt_X, nxt_Y)] = path[(curr_X, curr_Y)] + [(nxt_X, nxt_Y)]
                                        break
                            
    result = bfs(rectangle, matrix, characterX, characterY, itemX, itemY)
    answer = len(result)-1 # -start node
    return answer