def solution(n, times):
    '''
    binary search
    최적값 찾기, input이 너무 길때
    
    최소시간부터 최대시간 사이의 binary search
        - 1 ~ max(times)*n
    
    mid 시간에 심사 받은 사람이 n이 넘어가면 안됨
    
    '''
    
    left = 1 
    right = max(times) * n
    
    while left <= right:
        mid = (left+right)//2
        people = 0
        
        for time in times: # 각각 심사대에서 심사 받은 사람 계산
            people += mid//time
            
            if people >= n:
                break
        if people >= n:
            right = mid -1
            answer = mid # n명 이상 심사를 해야하는 것이기 때문에 여기에 answer = mid가 들어감
        else:
            # 여기에 answer = mid를 넣으면 안됨 만약 n명 이하의 최대 시간이라면 여기에 넣는게 맞을 듯?
            left = mid + 1
    
    return answer
