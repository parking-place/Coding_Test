def solution(clothes):
    answer = 1
    
    # 옷 종류별로 딕셔너리 생성
    closet = {}
    
    # 옷 종류별로 옷 갯수 저장
    for c in clothes:
        try:
            closet[c[1]] += 1
        except:
            closet[c[1]] = 1
            
        
        
    print(closet)
    
    # 옷들의 갯수 + 1을 모두 곱함 (+1은 옷을 안입는 경우)
    for k in closet.keys():
        answer *= closet[k] + 1
    
    # 아무것도 안입는 경우를 빼줌
    answer -= 1
    
    return answer