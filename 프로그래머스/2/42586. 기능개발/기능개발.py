def solution(progresses, speeds):
    answer = []
        
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        result = 0
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            result += 1
            if len(progresses) == 0:
                break
        if result != 0:
            answer.append(result)
    
    return answer