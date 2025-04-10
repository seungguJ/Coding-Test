from collections import deque
import copy
'''
같은 숫자끼리 인접해 있는 것들끼리 그룹
harmony(G1,G2) -> return (num(G1) + num(G2)) x value(G1) x value(G2)
초기 예술 점수: sum(harmony(combination(Group list, 2)))
회전:
1. 반시계 90도 회전
2. 중앙 십자 모양을 기준으로 4 개의 정사각형은 시계방향으로 90도 회전

function
- grouping (bfs) -> return [group1_index:list, group2_index:list]
- get_border
- harmony
- counter_clockwise
- clockwise
'''

N = int(input())

matrix = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)
    
def grouping(matrix):
    group_list = deque([])
    visited = set()
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for row in range(len(matrix)):
        for col in range((len(matrix[0]))):
            group = [] # [value, (x1, y1), ...]
            if (row, col) not in visited:
                curr_val = matrix[row][col]
                group.append(curr_val)
                visited.add((row,col))
                queue=deque([(row,col)])
                group.append((row,col))

                while queue:
                    curr_row, curr_col = queue.popleft()
                    for i in range(4):
                        nxt_row, nxt_col = curr_row+dx[i], curr_col+dy[i]
                        if 0 <= nxt_row < len(matrix) and 0 <= nxt_col < len(matrix[0]):
                            if (nxt_row, nxt_col) not in visited:
                                nxt_val = matrix[nxt_row][nxt_col]
                                if curr_val == nxt_val:
                                    queue.append((nxt_row,nxt_col))
                                    group.append((nxt_row,nxt_col))
                                    visited.add((nxt_row, nxt_col))
            
            if len(group) != 0:
                group_list.append(group)
    
    return group_list

def get_border(group1, group2):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    len_group1, len_group2 = len(group1), len(group2)
    count = 0
    if len_group1 < len_group2:
        for x,y in group1:
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if (nx, ny) in group2:
                    count+=1
    else:
        for x,y in group2:
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if (nx, ny) in group1:
                    count+=1
    return count

def harmony_score(group1, group2):
    group1_val = group1[0]
    group2_val = group2[0]
    num_border = get_border(group1[1:], group2[1:])

    return (len(group1[1:])+len(group2[1:])) * group1_val * group2_val * num_border

def counter_clockwise(matrix):
    N = len(matrix)
    new_matrix = copy.deepcopy(matrix)
    mid_idx = (N-1)//2
    '''
    new_matrix[mid_idx][0] <- matrix[0][mid_idx]
    new_matrix[0][mid_idx] <- matrix[mid_idx][N-1-0]
    '''

    for i in range(N):
        new_matrix[mid_idx][i] = matrix[i][mid_idx]
        new_matrix[i][mid_idx] = matrix[mid_idx][N-1-i]
    
    return new_matrix

def clockwise(matrix):
    N = len(matrix)
    new_matrix = copy.deepcopy(matrix)
    
    '''
    각 줄을 90도로 회전
    '''

    for col in range(N):
        for row in range(N):
            new_matrix[row][col] = matrix[N-1-col][row]
    
    return new_matrix

def combination(group):
    N = len(group)
    result = []
    for i in range(N):
        for j in range(i+1,N):
            result.append((i,j))
    return result

def get_new_matrix(matrix):
    new_matrix1 = counter_clockwise(matrix)

    p1, p2, p3, p4 = [], [], [], [] # partial mat
    for i in range((N-1)//2):
        t1, t2, t3, t4 = [], [], [], []
        for j in range((N-1)//2):
            t1.append(new_matrix1[i][j])
            t2.append(new_matrix1[i+(N-1)//2+1][j])
            t3.append(new_matrix1[i][j+(N-1)//2+1])
            t4.append(new_matrix1[i+(N-1)//2+1][j+(N-1)//2+1])
        p1.append(t1)
        p2.append(t2)
        p3.append(t3)
        p4.append(t4)

    new_p1 = clockwise(p1)
    new_p2 = clockwise(p2)
    new_p3 = clockwise(p3)
    new_p4 = clockwise(p4)

    for i in range((N-1)//2):
        for j in range((N-1)//2):
            new_matrix1[i][j] = new_p1[i][j]
            new_matrix1[i+(N-1)//2+1][j] = new_p2[i][j]
            new_matrix1[i][j+(N-1)//2+1] = new_p3[i][j]
            new_matrix1[i+(N-1)//2+1][j+(N-1)//2+1] = new_p4[i][j]
    
    return new_matrix1

group = grouping(matrix)
combi_list = combination(group)
score = 0
for combi in combi_list:
    i,j = combi[0], combi[1]
    score += harmony_score(group[i], group[j])

new_matrix1 = get_new_matrix(matrix)

group1 = grouping(new_matrix1)
combi_list = combination(group1)
score1 = 0
for combi in combi_list:
    i,j = combi[0], combi[1]
    score1 += harmony_score(group1[i], group1[j])

new_matrix2 = get_new_matrix(new_matrix1)

group2 = grouping(new_matrix2)
combi_list = combination(group2)
score2 = 0
for combi in combi_list:
    i,j = combi[0], combi[1]
    score2 += harmony_score(group2[i], group2[j])

new_matrix3 = get_new_matrix(new_matrix2)

group3 = grouping(new_matrix3)
combi_list = combination(group3)
score3 = 0
for combi in combi_list:
    i,j = combi[0], combi[1]
    score3 += harmony_score(group3[i], group3[j])

print(score+score1+score2+score3)