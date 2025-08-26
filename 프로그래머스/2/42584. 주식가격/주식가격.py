from collections import defaultdict, deque
def solution(prices):
    answer = deque([])
    
    tmp = deque([])
    for i in range(len(prices)):
        price = prices.pop()
        cnt = 0
        for j in tmp:
            cnt += 1
            if price > j:
                break
        answer.appendleft(cnt)
        tmp.appendleft(price)
    answer = list(answer)
    return answer