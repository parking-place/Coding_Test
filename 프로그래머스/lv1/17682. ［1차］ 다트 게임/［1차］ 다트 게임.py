import re

# 총점 계산 함수
def total_scoring(darts):
    # 총점, 스타상 중첩 횟수, 이전 스타상 여부, 스타상 여부, 샤프 여부 초기화
    total_score = 0
    is_pre_star = False
    is_star = False
    is_sharp = False
    
    # 역순으로 순회
    for i in range(len(darts)-1, -1, -1):
        
        # 점수, 보너스, 옵션 초기화
        score = int(darts[i][0])
        bonus = darts[i][1]
        option = darts[i][2]
        
        # 옵션 변수 초기화
        is_star = False
        is_sharp = False
        if option == '*':
            is_star = True
        elif option == '#':
            is_sharp = True
        
        # 보너스 점수 계산
        score = bonus_scoring(score, bonus)
        
        # 옵션 점수 계산
        score = option_scoring(score, is_star, is_pre_star, is_sharp)
        
        # 총점 계산
        total_score += score
        
        # 이전 스타상 여부 저장
        is_pre_star = is_star
    return total_score

# 보너스 점수 계산
def bonus_scoring(score, bonus):
    if bonus == 'S':
        return score
    elif bonus == 'D':
        return score ** 2
    elif bonus == 'T':
        return score ** 3
    
# 옵션 계산
def option_scoring(score, is_star, is_pre_star, is_sharp):
    stars = 0
    # 스타상 중첩 횟수 계산
    stars += 1 if is_star else 0
    stars += 1 if is_pre_star else 0
    # 아차상이면 음수로 변환
    is_sharp = -1 if is_sharp else 1
    # 점수 계산
    return score * is_sharp * (2 ** stars)

def solution(dartResult):
    # 점수, 보너스, 옵션 문자열을 추출하는 정규식
    # 각 점수, 보너스, 옵션은 하위 그룹으로 추출
    dart_p = re.compile(r'(\d+)([SDT])([*#]?)')
    
    # 점수, 보너스, 옵션 문자열을 리스트에 저장
    darts = dart_p.findall(dartResult)
    
    return total_scoring(darts)