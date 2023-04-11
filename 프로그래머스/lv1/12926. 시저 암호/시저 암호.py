def solution(s, n):
    answer = ''
    # 소문자 26자리 0~25
    str_l = 'abcdefghijklmnopqrstuvwxyz'
    # 대문자 26자리 0~25
    str_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for v in s :
        
        is_lower = True         # 소문자 확인 변수
        
        if v == ' ' :           # 공백일 경우 건너뜀
            answer += ' '
            continue
        
        i = str_l.find(v)       # 소문자에서 인덱스번호 i 찾기
        if i == -1 :            # 없을 경우 대문자에서 i 찾기
            is_lower = False    # 소문자 확인 변수
            i = str_u.find(v)
        
        new_i = i+n             # 인덱스 번호에 밀 숫자만큼 더함
        new_i %= 26             # 0~25 범위 벗어나면 나머지로 구함
        
        if is_lower :               # 대소문자 구분후 암호화된 문자열을 합침
            answer += str_l[new_i]
        else :
            answer += str_u[new_i] 
            
    return answer