def solution(arr, divisor):
    answer = [ v for v in arr if v % divisor == 0]
    answer.sort()
    if answer == []:
        answer = [-1]
    return answer