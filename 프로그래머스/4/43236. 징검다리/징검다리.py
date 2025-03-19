def solution(distance, rocks, n):
    answer = 0
    '''
    0 - dist 거리
    rocks -> 돌의 위치
    n개 제거
    각 바위 사이의 거리의 최솟값 중 가장 큰 값 return
    
    mid of tot_distance가 나오기 위해서 최소한 몇 개의 돌을 제거해야하는가
        만약 n개 초과로 제거해야한다면 mid가 너무 큰 것임
    '''
    rocks.sort()
    rocks.append(distance)
    left = 0
    right = distance
    while left<=right:
        mid = (left+right)//2
        prev = 0
        num_del = 0
        for rock in rocks:
            dist = rock - prev
            if dist < mid: # mid가 최소가 아님
                num_del += 1
                if num_del > n:
                    break
            else:
                prev = rock
        if num_del > n: # mid가 최소가 되기 위해서는 더 많은 돌을 삭제해야함 -> mid가 너무 큰 숫자임
            right = mid-1
        else:
            answer = mid
            left = mid+1
            
    return answer