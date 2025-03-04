import heapq
def solution(jobs):
    answer = 0
    '''
    소요시간 -> 요청 시각 -> 작업 번호 작은 것
    turnaround time -> finish time - requested time
    return average of turnaround time: integer
    
    jobs: [requested time, required time]
    standby: 대기 큐 (요청 시각이 지난 job) -> heap[required time, requested time, idx(작업번호)]
    processing -> standby.pop(0) -> processing[required time] -= 1
        
    '''
    
    time = 0
    standby = []
    fin = 0 # finish flag
    idx = 0 # 작업번호
    tot_len = len(jobs)
    processing = []
    
    while tot_len != fin:
        if len(jobs) != 0:
            popped_list = []
            for i in range(len(jobs)):
                if jobs[i][0] == time:
                    tmp = [jobs[i][1], jobs[i][0], i]
                    heapq.heappush(standby, tmp)
                    popped_list.append(jobs[i])
            for i in range(len(popped_list)):
                jobs.remove(popped_list[i])
                        
        if len(processing) == 1:
            
            if processing[0][0] == 0:
                fin+=1
                answer += time-processing[0][1]
                processing.pop()

        if len(processing) == 0: # when in_processing is empty
            if len(standby) != 0:
                nxt = heapq.heappop(standby)
                processing.append(nxt)                
                
        time += 1
        if len(processing) == 1:
            processing[0][0] -= 1
    answer = answer//tot_len
    return answer