players = {}
n_ = 0

# DFS 방식으로 승리(혹은 패배)쪽으로 탐색, 결과를 자기 자신에게 업데이트
# 탐색 후 결정 가능 상태를 업데이트한다.
def dfs_w_or_l(p, w_or_l : str):
    global players, n_
    # 승리(혹은 패배)한 선수들의 리스트
    wl_l = list(players[p][w_or_l])
    # 승리(혹은 패배)한 선수들이 없으면 빈 집합 반환
    if wl_l == []:
        return set()
    
    # 이전에 탐색한 경우 탐색 결과 반환
    if players[p]['is_visit'][w_or_l]:
        return players[p][w_or_l]
    
    # 결정 가능 상태 업데이트
    if n_ == len(players[p]['win']) + len(players[p]['lose']) + 1:
        players[p]['is_decision'] = True
        
    # 플레이어가 순위를 매길 수 있는 상태이면 승리(혹은 패배)한 선수들을 반환
    if players[p]['is_decision'] == True:
        return players[p][w_or_l]
    
    # 승리(혹은 패배)한 선수들의 승리(혹은 패배)한 선수들을 재귀적으로 탐색
    # 탐색한 결과를 승패 집합에 업데이트
    for p_ in wl_l:
        players[p][w_or_l].update(dfs_w_or_l(p_, w_or_l))
        
    # 결정 가능 상태 업데이트
    if n_ == len(players[p]['win']) + len(players[p]['lose']) + 1:
        players[p]['is_decision'] = True
    
    players[p]['is_visit'][w_or_l] = True
    # 승리(혹은 패배)한 선수들의 승리(혹은 패배)한 선수들을 반환
    return players[p][w_or_l]


def solution(n, results):
    global players, n_
    n_ = n
    # 선수 번호를 키로 하는 딕셔너리 생성
    # 값은 다른 선수 번호들과의 승패 여부 딕셔너리
    players = { k : {'win' : set(), 'lose' : set() , 'is_decision' : False, 'is_visit':{'win':False, 'lose':False}} for k in range(1, n+1)}
    
    # 승패 결과를 딕셔너리에 저장
    for result in results:
        players[result[0]]['win'].add(result[1])
        players[result[1]]['lose'].add(result[0])
    
    for p in players.keys():
        # 승+패+자신 = 모든 플레이어인 경우 결정 가능
        if n_ == len(players[p]['win']) + len(players[p]['lose']) + 1:
            # 결정 가능 상태를 True로 변경
            players[p]['is_decision'] = True
            continue
        # 승리 상태와 패배 상태를 DFS를 통해 업데이트
        players[p]['win'].update(dfs_w_or_l(p, 'win'))
        players[p]['lose'].update(dfs_w_or_l(p, 'lose'))
        
    # 순위를 매길 수 있는 선수들의 수를 반환
    answer = sum(players[p]['is_decision'] for p in players.keys())
    return answer