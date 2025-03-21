def solution(word):
    answer = 0
    '''
    first digit (5*5*5*5+5*5*5+5*5+5)+1
    second digit (5*5*5+5*5+5)+1
    ...
    
    AE -> (5*5*5*5+5*5*5+5*5+5)+1 + 1 + (5*5*5+5*5+5)+1
    '''
    # word_list = ["A","E","I","O","U"]
    # temp=[0 for i in range(5)]
    # for i in range(len(word)):
    #     answer+=1
    #     idx = word_list.index(word[i])
    #     if i == 0:
    #         answer += 781*idx
    #     elif i == 1:
    #         answer += 156*idx
    #     elif i == 2:
    #         answer += 31*idx
    #     elif i == 3:
    #         answer += 6*idx
    #     else:
    #         answer += idx

    '''
    recursive
    
    '''
    word_list = ["A","E","I","O","U"]
    
    def dfs(word_list, current_word, visited):
        visited.append(current_word)
        if len(current_word) == 5:
            return
        for i in word_list:
            dfs(word_list, current_word+i, visited)
    visited = []
    dfs(word_list, "", visited)
    answer = visited.index(word)
    return answer