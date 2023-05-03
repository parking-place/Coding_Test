import sys
input = sys.stdin.readline
# 버튼 종류
buttons = [300, 60, 10]
# 버튼을 누른 횟수를 저장할 리스트
push_count = [0, 0, 0]
# 시간을 입력받는다.
time = int(input().rstrip())
# 버튼을 누른 횟수를 계산한다.
for i in range(3):
    c, t = divmod(time, buttons[i])
    push_count[i] = c
    time = t
# 시간이 0이면 버튼을 누른 횟수를 출력하고 아니면 -1을 출력한다.
print(*push_count, sep=' ') if time == 0 else print(-1)