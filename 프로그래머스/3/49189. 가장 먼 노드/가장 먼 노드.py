def solution(n, edge):
    answer = 0
    '''
    1번에서 가장 멀리 떨어진 노드의 갯수 구하기
    n: number of node
    edge: 2 dim of matrix
    '''
    '''
    1부터 시작해서 1-n의 숫자 중에서 지우면서 출발하기
    1 -> 2,3 then, remained: (4,5,6)
    '''
    
    remained_node = list(range(1,n+1))
    edge_dict = {}
    for ele in edge:
        ele.sort()
        if ele[0] not in edge_dict.keys():
            edge_dict[ele[0]] = [ele[1]]
        else:
            edge_dict[ele[0]].append(ele[1])
    print(edge_dict)
    return answer