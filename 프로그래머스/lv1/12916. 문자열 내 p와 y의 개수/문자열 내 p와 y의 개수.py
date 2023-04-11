def solution(s):
    answer = 0
    for i in range(len(s)) :
        if s[i] == 'p' or s[i] == 'P' :
            answer += 1
        elif s[i] == 'y' or s[i] == 'Y' :
            answer -= 1
    return not answer