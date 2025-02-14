def solution(n, results):
    answer = 0
    '''
    winneer_dict, loser_dict
    winner_dict 합칠 때 일반 for문으로 하면 안됨
    [[1, 2], [4, 5], [3, 4], [2, 3]] 같은 경우 1은 2 3 4 5 모두 이겼지만
    2와 3만 이겼다고 할 수 있음
    
    dfs로 구현
    '''
    winner_dict, loser_dict = {}, {}
    for i in range(len(results)):
        winner = results[i][0]
        loser = results[i][1]
        
        if winner not in winner_dict.keys():
            winner_dict[winner] = set([loser])
        else:
            winner_dict[winner].add(loser)
        if loser not in loser_dict.keys():
            loser_dict[loser] = set([winner])
        else:
            loser_dict[loser].add(winner)
    
    def dfs(results_dict, current_key, memo):
        if current_key in memo:
            return memo[current_key]  # 캐시된 결과 반환
        
        if current_key not in results_dict:
            memo[current_key] = set()  # 기록하여 중복 호출 방지
            return set()
        
        group = set(results_dict[current_key])
        for next_key in results_dict[current_key]:
            group.update(dfs(results_dict, next_key, memo))
        
        memo[current_key] = group  # 결과 저장
        return group
        
    total_winner_dict = {}
    total_loser_dict = {}
    for i in range(1, n+1):
        count = 0
        if i in winner_dict.keys():
            total_winner_dict[i] = dfs(winner_dict, i, total_winner_dict)
            count += len(total_winner_dict[i])
        if i in loser_dict.keys():
            total_loser_dict[i] = dfs(loser_dict, i, total_loser_dict)
            count += len(total_loser_dict[i])
        if count == n-1:
            answer += 1

        
    return answer