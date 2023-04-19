def solution(s):    
    # 문자열 길이가 홀수이거나, 첫번째 문자가 ')'이거나, 마지막 문자가 '('이면 False
    if s[0] == ')' or s[-1] == '(' or len(s) % 2 != 0:
        return False
    
    total = 0
    
    for v in s:
        if v == '(':
            total += 1
        else:
            total -= 1
        
        # ')'가 더 많아지면 False
        if total < 0:
            return False
    
    # '('와 ')'의 개수가 같지 않으면 False
    if total != 0:
        return False

    return True

n = int(input())
for _ in range(n):
    is_vps = solution(input())
    result = 'YES' if is_vps else 'NO'
    print(result)