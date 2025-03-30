from collections import deque
def solution(people, limit):
    answer = 0
    '''
    한 구명 보트 당 최대 2명, 무게 제한
    최소 구명보트 개수
    
    limit //2 를 기준으로 나눔 -> 절반 이하, 절반 이상
    low.sort(), high.sort(reverse=True) -> queue
    둘 중 작은 갯수로 시작
    while min(low, high):
        if low[0] + high[0] <= limit:
            low.pop, high.pop
            answer += 1
        else:
            high.pop
            answer += 1
        
    '''
    
    mid = limit / 2
    low, high, mid_people = [], [], []
    num_low, num_high, num_middle = 0, 0, 0
    for i in people:
        if i < mid:
            num_low += 1
            low.append(i)
        elif i == mid:
            num_middle += 1
            mid_people.append(i)
        else:
            num_high += 1
            high.append(i)
    low.sort()
    high.sort(reverse=True)
    low_queue = deque(low)
    high_queue = deque(high)
    
    while num_low != 0 and num_high != 0:
        if low_queue[0] + high_queue[0] <= limit:
            low_queue.popleft()
            high_queue.popleft()
            num_low -= 1
            num_high -= 1
            answer += 1
        else:
            high_queue.popleft()
            num_high -= 1
            answer += 1
    if num_low != 0:
        answer += num_low/2
    if num_high != 0:
        answer += num_high
    answer += num_middle/2
    answer = round(answer+0.1)
    
    return answer