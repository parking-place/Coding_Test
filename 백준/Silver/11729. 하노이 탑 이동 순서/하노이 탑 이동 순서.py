# 원판의 갯수 n, 시작 기둥 start, 끝 기둥 end, 보조 기둥 sub
# 재귀적으로 작동
def hanoi(n, start, end, sub):
    global move_list
    # 원판이 1개일 경우, 시작 기둥에서 끝 기둥으로 이동
    if n == 1:
        print(f'{start} {end}')
    # 원판이 1개가 아닐 경우
    else:
        # n-1개의 원판을 시작 기둥에서 보조 기둥으로 이동
        hanoi(n-1, start, sub, end)
        # 마지막 원판을 시작 기둥에서 끝 기둥으로 이동
        print(f'{start} {end}')
        # 보조 기둥에 있는 n-1개의 원판을 끝 기둥으로 이동
        hanoi(n-1, sub, end, start)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)