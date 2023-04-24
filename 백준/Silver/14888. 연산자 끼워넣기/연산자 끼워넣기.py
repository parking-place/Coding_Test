from collections import deque

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiple(a, b):
    return a * b

def divide(a, b):
    # 둘중 하나만 음수일 때
    if (a > 0) ^ (b > 0):
        return -(a // -b)
    else:
        return a // b

# 결과 딕셔너리
results_dict = {}
# 사칙연산 문자열 리스트
orders = ['+', '-', '*', '/']
# 사칙연산 함수를 리스트에 저장
oper = [plus, minus, multiple, divide]

# 연산 재귀 함수
def calculate(nums_qu : deque, opers_count : int, order_str = ''):
    global results_dict, oper
    
    # 넘겨받은 숫자 큐의 길이가 1이면
    if len(nums_qu) == 1:
        # 결과를 저장하고 리턴
        results_dict[order_str] = nums_qu[0]
        return
    
    # 사칙연산을 수행
    for i in range(4):
        # 값 복사 시행
        n_q, o_c = deque(nums_qu), list(opers_count)
        o_s = order_str
        # 해당 연산이 없으면 다음 연산자로 넘어감
        if o_c[i] == 0:
            continue
        # 연산자를 문자열에 추가
        o_c[i] -= 1
        # 연산자를 문자열에 추가(딕셔너리의 키로 사용)
        o_s += orders[i]
        
        # 연산 수행
        a = n_q.popleft()
        n_q[0] = oper[i](a, n_q[0])
        
        # 재귀 함수 호출
        calculate(n_q, o_c, o_s)



# 숫자의 개수
n = int(input())
# 숫자 입력
nums = list(map(int, input().split()))
# 사칙연산의 갯수 입력
opers_count = list(map(int, input().split()))
# 연산 수행
calculate(deque(nums), opers_count)
# 결과 출력
print(max(results_dict.values()))
print(min(results_dict.values()))