n = int(input())

# n을 입력받아 2진수로 변환하여 출력하는 함수
def to_binary(n):
    # n이 0이면 빈 문자열을 반환
    if n == 0:
        return ''
    # n//2는 to_binary()에 넣어 재귀적으로 호출
    # n%2는 2로 나눈 나머지를 문자열로 변환하여 더함
    return to_binary(n//2) + str(n%2)

print(to_binary(n))