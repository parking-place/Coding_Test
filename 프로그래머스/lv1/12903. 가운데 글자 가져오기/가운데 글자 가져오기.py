def solution(s):
    answer = ''
    lenth = len(s)
    half = lenth//2
    if lenth % 2 != 0 :
        answer = s[half]
    else :
        answer = s[half-1:half+1]
    return answer