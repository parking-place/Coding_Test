# 피보나치를 저장 할 딕셔너리
fibonacci_dict = {
    1 : 1,
    2 : 1
}

def fibonacci(n) :
    # 딕셔너리에서 먼저 확인
    if n in fibonacci_dict :
        return fibonacci_dict[n]         

    # 없는경우에만 재귀를 이용해 구함
    result = fibonacci(n-1) + fibonacci(n-2)
    # 이미 구해진 값들을 참조하므로 성능상 이점이 큼
    fibonacci_dict[n] = result
    return result

def solution(n):
    # 3부터 n까지 피보나치 수를 구함
    for i in range(3, n+1):
        answer = fibonacci(i)
    return answer % 1234567