def solution(a, b):
    answer = 0
    
    answer = sum(list(range(min(a,b), max(a,b)+1)))
    
    return answer
