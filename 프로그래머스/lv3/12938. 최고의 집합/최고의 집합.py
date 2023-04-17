def solution(n, s):
    answer = []
    q, r = divmod(s, n)
    
    if q == 0: return [-1]
    
    for _ in range(n):
        answer.append(q)
    for i in range(n-r, n):
        answer[i] += 1
    return answer