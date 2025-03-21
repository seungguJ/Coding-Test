def solution(word):
    answer = 0
    '''
    first digit (5*5*5*5+5*5*5+5*5+5)+1
    second digit (5*5*5+5*5+5)+1
    ...
    
    AE -> (5*5*5*5+5*5*5+5*5+5)+1 + 1 + (5*5*5+5*5+5)+1
    '''
    word_list = ["A","E","I","O","U"]
    temp=[0 for i in range(5)]
    for i in range(len(word)):
        answer+=1
        idx = word_list.index(word[i])
        if i == 0:
            answer += 781*idx
        elif i == 1:
            answer += 156*idx
        elif i == 2:
            answer += 31*idx
        elif i == 3:
            answer += 6*idx
        else:
            answer += idx
            
    return answer