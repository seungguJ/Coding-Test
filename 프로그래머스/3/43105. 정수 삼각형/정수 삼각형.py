def solution(triangle):
    answer = 0
    '''
    
    처음과 끝 -> 한가지의 길 밖에 없음
    중간 부분 -> 위의 두 길 중에서 더 큰 값만 저장
    
    result: 결과 저장
    이전 triangle 숫자 개수 만큼 저장되어있음
    
    for i=0 to len(triangle) do
        tmp = []
        for j=0 to len(triangle[i][j])
            if j == 0
                tmp.append(result[0] + triangle[i][j])
            elif j == len(triangle[i][j])
                tmp.append (result[-1] + triangle[i][j])
            else
                val = max(result[j-1], result[j])+triangle[i][j]
                tmp.append(val)
                
    '''
    
    result = []
    result.append(triangle[0][0])
    
    for i in range(1,len(triangle)):
        tmp = []
        for j in range(len(triangle[i])):
            if j == 0:
                tmp.append(result[0]+triangle[i][j])
            elif j == len(triangle[i])-1:
                tmp.append(result[-1]+triangle[i][j])
            else:
                max_val = max(result[j-1], result[j])
                tmp.append(max_val+triangle[i][j])
        result = tmp
    
    answer = max(result)

    return answer