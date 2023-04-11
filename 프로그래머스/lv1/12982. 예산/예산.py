def solution(d, budget):
    answer = 0
    d.sort()
    for v in d:
        budget -= v
        if budget < 0:
            break
        answer += 1
    return answer