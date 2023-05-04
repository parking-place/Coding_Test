import sys
from collections import deque
input = sys.stdin.readline
# n : 회의의 수
n = int(input().rstrip())
# 회의들의 정보를 저장할 리스트
meetings = []
# 회의들의 정보를 입력받는다.
for _ in range(n):
    s, e = map(int, input().rstrip().split())
    meetings.append((s, e))
# 회의들을 시작시간을 기준으로 정렬한다.
meetings.sort(key=lambda x: x[0])
# 회의들을 끝나는 시간을 기준으로 재정렬한다.
meetings.sort(key=lambda x: x[1])
# 회의들을 앞에서부터 확인할 것이므로 큐로 만든다.
meetings = deque(meetings)
# 시작시간으로 정렬 후, 끝나는 시간으로 정렬하면
# 끝나는 시간이 같은 회의들은 시작시간이 빠른 순서대로 정렬된다.
# 즉, 순서대로 확인해가며 시작시간이 끝나는 시간보다 크거나 같으면,
# 진행할 수 있는 회의중 가장 빨리 끝나는 회의를 진행한다
# 최선의 선택(그리디) -> 가능한 많은 회의를 진행할 수 있다.

# 한 회의실에서 진행한 회의의 수
count = 0
# 마지막으로 진행한 회의의 끝나는 시간
time = 0
# 회의들을 확인한다.
while meetings:
    # 현재 회의를 가져온다.
    meeting = meetings.popleft()
    # 현재 회의를 진행할 수 있으면 진행한다.
    if time <= meeting[0]:
        count += 1
        time = meeting[1]
# 회의의 수를 출력한다.
print(count)