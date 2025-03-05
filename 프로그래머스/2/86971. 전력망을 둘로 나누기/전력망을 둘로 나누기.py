def solution(n, wires):
    answer = -1
    '''
    n개의 트리 -> 선을 끊어서 네트워크 2개로 분리(송전탑 개수 비슷하게)
    
    n: 송전탑 개수
    wires: 전선 정보
    return 송전탑 개수의 차이
    
    sol (n-> 범위 작음 -> 완전탐색)
    for wire in wires:
        tmp = wires.copy()
        tmp.remove(wire)
        make_tree -> set1, set2
        return len(set1)-len(set2)
    '''
    for wire in wires:
        tmp = wires.copy()
        tmp.remove(wire)
        
        update_flag = True
        set1 = set()
        set1.update(tmp[0])
        
        while update_flag:
            update_flag = False
            for ele in tmp:
                v1 = ele[0]
                v2 = ele[1]
                if v1 in set1 or v2 in set1:
                    new_set = set1.union(set(ele))
                    if len(new_set) != len(set1):
                        update_flag = True
                        set1.update(ele)
                        break
                    else:
                        continue

        len_s2 = n-len(set1)
        result = abs(len(set1)-len_s2)
        if answer == -1:
            answer = result
        elif answer > result:
            answer = result
        else:
            pass
    
    return answer