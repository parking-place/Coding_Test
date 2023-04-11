def is_harshad(n):
    # 자릿수 별로 나누기
    l = list(str(n))
    l = list(map(int, l))
    # 자릿수의 합으로 나누어 떨어지면 True
    return n % sum(l) == 0

def solution(x):
    return is_harshad(x)