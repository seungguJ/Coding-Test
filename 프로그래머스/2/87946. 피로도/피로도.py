from itertools import permutations
def solution(k, dungeons):
    answer = -1
    k_ori = k
    for sequences in permutations(range(len(dungeons))):
        k = k_ori
        result = 0

        for num in sequences:
            min_fat, consumed = dungeons[num]
            if k < min_fat:
                break
            else:
                k-=consumed
                result+=1
        if result > answer:
            answer = result
                
    return answer