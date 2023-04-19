def solution(s):
    l = [int(v) for v in s.split(' ')]
    min_ = min(l)
    max_ = max(l)
    answer = str(min_) + ' ' + str(max_)
    return answer