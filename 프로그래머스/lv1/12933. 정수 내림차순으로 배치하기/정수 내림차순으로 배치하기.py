def solution(n):
    answer = ''
    l = list(str(n))
    l.sort(reverse=True)
    for v in l:
        answer += v
    return int(answer)