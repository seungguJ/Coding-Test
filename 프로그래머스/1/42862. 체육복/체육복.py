def solution(n, lost, reserve):
    answer = 0
    '''
    우선순위
    1. 자기 자신이 잃어버린사람
    2. 한 명만 빌려줄 수 있는 사람
    3. 두 명 빌려줄 수 있는 사람
    '''
    borrow1, borrow2 = [], []
    for num in reserve:
        if num in lost:
            lost.remove(num)
        elif num-1 in lost and num+1 in lost:
            borrow2.append(num)
        elif num-1 or num+1 in lost:
            borrow1.append(num)
        else:
            pass

    for num in borrow1:
        if num-1 in lost:
            lost.remove(num-1)
        elif num+1 in lost:
            lost.remove(num+1)
            
    for num in borrow2:
        if num-1 in lost:
            lost.remove(num-1)
        elif num+1 in lost:
            lost.remove(num+1)        
    
    answer = n-len(lost)
    
    return answer