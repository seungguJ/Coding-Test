from collections import deque
def solution(number, k):
    answer = ''
    '''
    k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
    앞에서부터 가장 큰 숫자 찾아가기
    뒤에 남은 숫자 고려
    
    
    '''
    # while k:
    #     if len(number) == k: # remove all remained number
    #         number = ""
    #         break
    #     tmp = [int(i) for i in number[:k+1]]
    #     max_val = str(max(tmp))
    #     answer+=max_val
    #     idx = tmp.index(int(max_val))
    #     k-= idx # remained number can be removed
    #     number=number[idx+1:] # remained number
    # answer += number
    
    
    '''
    O(n)으로 풀어야합
    stack 사용
    현재 값이 이전 값보다 크면 pop and append
    '''
    stack = []
    for i in range(len(number)):
        if len(stack) == 0:
            stack.append(number[i])
        else:
            while int(stack[-1]) < int(number[i]):
                stack.pop()
                k-=1
                if len(stack) == 0 or k == 0:
                    break
            stack.append(number[i])
        if k == 0:
            break
    while k != 0:
        stack.pop()
        k-=1
    answer = answer.join(stack)
    number = number[i+1:]
    answer += number
    return answer