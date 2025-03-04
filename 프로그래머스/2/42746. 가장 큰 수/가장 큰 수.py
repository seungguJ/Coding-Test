def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    sorted_list = sorted(numbers, key=lambda x: x*5)
    sorted_list.reverse()
    for num in sorted_list:
        answer += str(num)
    answer = str(int(answer))
    return answer