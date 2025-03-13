from collections import deque
def solution(begin, target, words):
    answer = 0
    '''
    가장 짧은 변환 과정 -> bfs
    글자 하나만 다른 것을 바꿔야함 -> def is_val
    
    bfs
    visited
    queue
    
    for word in words:
        if is_val(word):
            queue.append(word)
            visited.add(word)
    '''
    
    def is_val(word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count == 1:
            return True
        else:
            return False
    
    if target not in words:
        return 0
    
    def bfs(words, begin, target):
        visited = []
        queue = deque([(begin,[begin])])
        while queue:
            curr_word, path = queue.popleft()
            if curr_word == target:
                return path
            for word in words:
                if is_val(curr_word,word):
                    queue.append((word, path+[word]))
                    visited.append(word)
    
    result = bfs(words, begin, target)
    answer = len(result)-1
    
    return answer