from heapq import heapify, heappush, heappop
def solution(scoville, K):
    answer = 0
    '''
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        ing1 = scoville.pop(0)
        ing2 = scoville.pop(0)
        if ing2 == 0:
            answer = -1
            break
        else:
            new_ing = ing1 + 2*ing2
            scoville.insert(0,new_ing)
            scoville.sort()
            answer+=1
    '''
    heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        ing1 = heappop(scoville)
        ing2 = heappop(scoville)
        if ing2 == 0:
            answer = -1
            break
        new_ing = ing1 + 2*ing2
        heappush(scoville, new_ing)
        answer += 1
    return answer