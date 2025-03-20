import heapq
def solution(operations):
    answer = []
    heap = []
    for operation in operations:
        if operation.startswith('I'):
            number = int(operation[2:])
            heapq.heappush(heap, number)
        else: # startswith 'D'
            if operation[2] == '-': # delete min val
                if len(heap) != 0:
                    heapq.heappop(heap)
            else: # delete max value
                if len(heap) != 0:
                    tmp = [-i for i in heap]
                    heapq.heapify(tmp)
                    heapq.heappop(tmp)
                    heap = [-i for i in tmp]
                    heapq.heapify(heap)
    if len(heap) == 0:
        return [0,0]
    elif len(heap) == 1: # if only one element, min val == max val
        return [heap[0],heap[0]]
    else:
        min_val = heapq.heappop(heap)
        tmp = [-i for i in heap]
        heapq.heapify(tmp)
        max_val = -heapq.heappop(tmp)
        return [max_val, min_val]
    return answer