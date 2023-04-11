def solution(phone_number):
    answer = ''
    behind = phone_number[-4:]
    answer = '*' * (len(phone_number) - 4) + behind
    return answer