def solution(k, tangerine):
    answer = 0
    
    # 귤 크기를 key로, 귤 갯수를 value로 하는 딕셔너리
    t_d = {}
    # 값을 채워넣기
    for t in tangerine:
        # 귤 크기가 있는 경우, 갯수를 1 증가
        try:
            t_d[t] += 1
        # 귤 크기가 없는 경우, 0으로 초기화
        except:
            t_d[t] = 1
    
    # 귤 크기를 기준으로, 내림차순으로 정렬
    t_d = sorted(t_d.values(), reverse=True)

    # 귤을 양이 많은 크기부터 상자에 담기
    for v in t_d:
        # 상자에 귤을 담을 수 없는 경우, break
        if k <= 0:
            break
        # 상자에 귤을 담을 수 있는 경우, 담음
        else:
            answer += 1
            k -= v
    
    return answer