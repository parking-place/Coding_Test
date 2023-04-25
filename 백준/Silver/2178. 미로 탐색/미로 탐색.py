from collections import deque
from pprint import pprint

# 이동함수들 정의
def go_pos_x(x, y):
    x_ = x + 1
    if x == n-1: return False
    if maze[x_][y] == '0': return False
    if maze_distances[x_][y] != -1: return False
    return x_, y
def go_nag_x(x, y):
    x_ = x - 1
    if x == 0: return False
    if maze[x_][y] == '0': return False
    if maze_distances[x_][y] != -1: return False
    return x_, y
def go_pos_y(x, y):
    y_ = y + 1
    if y == m-1: return False
    if maze[x][y_] == '0': return False
    if maze_distances[x][y_] != -1: return False
    return x, y_
def go_nag_y(x, y):
    y_ = y - 1
    if y == 0: return False
    if maze[x][y_] == '0': return False
    if maze_distances[x][y_] != -1: return False
    return x, y_

# 이동 함수들을 리스트로 묶음
go_funcs = [go_pos_x, go_nag_x, go_pos_y, go_nag_y]

n,m = map(int,input().split())
# 미로 입력
maze = []
for _ in range(n):
    maze.append(list(input()))
# 거리와 방문여부를 담는 리스트
# 미방문시 -1, 방문시 거리를 담음
maze_distances = [[-1] * m for _ in range(n)]
# 시작점 큐에 넣기, 거리 1로 초기화
qu = deque()
qu.append((0,0))
maze_distances[0][0] = 1
while qu:
    x, y = qu.popleft()
    for go in go_funcs:
        # 이동할 수 없는 경우, 다음 이동 함수로 넘어감
        if not bool(go(x,y)):
            continue
        # 이동할 수 있는 경우
        # 이동 후 거리를 1 증가
        # 좌표를 큐에 넣음
        x_, y_ = go(x,y)
        maze_distances[x_][y_] = maze_distances[x][y] + 1
        qu.append((x_, y_))
        
print(maze_distances[n-1][m-1])