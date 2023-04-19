# 문자열 s가 균형잡힌 괄호 문자열인지 판단하는 함수
# 빈 문자열이면 False를 반환
def is_balanced(s):
    if s != '':
        if s.count('(') == s.count(')'):
            return True
    return False

# 문자열 s가 올바른 괄호 문자열인지 판단하는 함수
# 이미 균형잡힌 괄호 문자열이라고 가정
# 스택을 이용하여 판단 -> 이전 문제에서 사용한 방법
def is_correct(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(p)
        else:
            try:
                stack.pop()
            except:
                return False
    if stack != []:
        return False
    return True  

# 4-4 단계에서 사용하는 함수
def del_and_reverse(s):
    # 문자열의 첫 번째와 마지막 문자를 제거
    s = s[1:-1]
    # 나머지 문자열의 괄호 방향을 뒤집기
    s = [')' if p == '(' else '(' for p in s]
    # 리스트를 문자열로 변환
    s = ''.join(s)
    return s

# 문자열 s를 올바른 괄호 문자열로 변환하는 함수
def to_correct(s):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if s == '': return ''
    for i in range(len(s)+1):
        if is_balanced(s[:i]):
            # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
            # i가 문자열의 길이 + 1 과 같다면 u = s, v = ''
            u, v = (s[:i], s[i:]) if i != len(s)+1 else (s, '')
            if is_correct(u):
                # 3. 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
                # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
                print(u, v)
                return u + to_correct(v)
            else:
                # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
                    # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
                    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
                    # 4-3. ')'를 다시 붙입니다. 
                    # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
                    # 4-5. 생성된 문자열을 반환합니다.
                return '(' + to_correct(v) + ')' + del_and_reverse(u)
        
def solution(p):
    answer = to_correct(p)
    return answer