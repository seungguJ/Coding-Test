def solution(s):
    answer = True
    
    tmp_list = []
    for i in range(len(s)):
        if s[i] == '(':
            tmp_list.append(s[i])
        else:
            if len(tmp_list) == 0:
                return False
            else:
                tmp_list.pop()
    if len(tmp_list) != 0:
        return False
    return True