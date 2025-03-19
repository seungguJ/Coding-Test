from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    '''
    모든 트럭이 다리를 건너기 위해서 최소 몇 초가 걸리는지
    bridge_length: 길어
    weight이하 무게
    
    대기, 현재 큐
    현재 큐 = [ [kg,남은길이] ]
    
    tot_kg = 0
    while 대기 and 현재 큐
        time += 1
        
        for i in 현재 큐 ind:
            현재 큐[i][1] -= 1
        
        if 현재 큐[0][1] == 0:
            tot_kg -= 현재 큐[0][0]
            현재 큐.popleft()
            
        if tot_kg + 1번대기_kg > weight:
            pass
        else:
            현재 큐.append([truck_weight])
            tot_kg += 대기.popleft()
       
    '''
    
    ready_queue = deque(truck_weights)
    first_truck = ready_queue.popleft()
    curr_queue = deque([[first_truck, bridge_length]])
    tot_kg = first_truck
    time = 0
    
    while len(ready_queue)!=0 or len(curr_queue)!=0:
        time += 1
        
        if len(curr_queue) != 0:
            for i in range(len(curr_queue)):
                curr_queue[i][1] -= 1
        
        if curr_queue[0][1] == -1: # 트럭이 모두 빠져 나가야함 -> 실제로 bridge_length+1의 길이만큼 가야함
            tot_kg -= curr_queue[0][0]
            curr_queue.popleft()
        
        if time != 1: # while문 전에 curr_queue에 트럭을 넣어버려서 첫 시간만 제외
            if len(ready_queue) != 0:
                if tot_kg + ready_queue[0] <= weight:
                    nxt_truck = ready_queue.popleft()
                    tot_kg += nxt_truck
                    curr_queue.append([nxt_truck, bridge_length-1])
                else:
                    pass
        
    answer = time

    return answer