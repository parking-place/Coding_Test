# 광물의 처리량을 저장한 딕셔너리
m_d = { 'diamond': 25, 'iron': 5, 'stone': 1 }

# unit과 pick의 meterial을 받아서, 피로도를 반환하는 함수
def process_unit(meterial, unit):
    
    # print(meterial, unit)
    
    # unit의 각 광물의 처리량을, pick의 재질에 따라서 처리
    unit = [ int(v//m_d[meterial]) for v in unit ]
    
    # 처리량이 0이면, 1로 변경
    unit = [ 1 if v == 0 else v for v in unit ]
    
    # print(unit)
    # print(sum(unit))
    
    # 총 처리량을 반환
    return sum(unit)


def solution(picks, minerals):
    answer = 0
    
    # pick의 종류와 갯수를 저장한 딕셔너리
    # process_unit 함수에서, pick을 사용하기 위해, 딕셔너리로 저장
    picks_d = { 
        'diamond': picks[0],
        'iron': picks[1],
        'stone': picks[2]
        }
    
    # 광물 순서 리스트를 5개씩 나누어서 저장할 리스트
    minerals_units = []
    
    # 광물을 5개씩 나누어서 저장
    # 5개 씩 나누어 저장하면, 하나의 처리단위(unit)로 묶일 수 있음
    # 광물 명을 숫자로 바꾸어서 저장
    for i in range(len(minerals)):
        if i % 5 == 0:
            minerals_units.append([])
        minerals_units[-1].append(m_d[minerals[i]])
        
    # pick의 갯수만큼의 unit을 처리 가능하므로, 그 뒤의 unit은 처리할 필요가 없음
    if sum(picks) < len(minerals_units):
        minerals_units = minerals_units[:sum(picks)]
        
    # 처리 가능한 unit 끼리는 순서를 바꿀 수 있으므로, 
    # 피로도를 최소화하기 위해, 다이아, 철, 돌이 많은 순서대로 정렬
    # 유닛들을 정렬 할 경우, 가장 좋은 pick부터 처리하면 됨.
    minerals_units.sort(key=lambda unit: sum(unit), reverse=True)
    
    # 유닛 처리
    for meterial, pick in picks_d.items():
        # 비싼 pick부터, pick의 갯수만큼 처리
        for i in range(pick):
            # 처리할 unit이 없으면, break
            if len(minerals_units) == 0:
                break            
            
            # pcik의 재질과, 처리할 unit을 매개변수로, process_unit 함수 호출
            # 반환된 피로도를 answer에 더함
            answer += process_unit(meterial, minerals_units.pop(0))
    
    return answer