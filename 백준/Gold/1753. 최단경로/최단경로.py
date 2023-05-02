import sys
input = sys.stdin.readline
# 우선순위 큐를 이용한 다익스트라 알고리즘
from queue import PriorityQueue

# 노드의 개수, 간선의 개수, 시작 노드 번호를 입력받기
n_c, e_c = map(int, input().rstrip().split())
s = int(input().rstrip())
# 시작 노드로부터 각 노드까지의 거리를 담을 리스트
dists = [999_999_999] * (n_c + 1)
# 방문여부를 체크할 리스트
visits= [False] * (n_c + 1)
# 각 노드에 연결된 간선 정보를 담을 리스트
# (거리, 노드 번호) 형태로 저장
edges = [[] for _ in range(n_c + 1)]
# 모든 간선 정보 입력받기
for _ in range(e_c):
    u, v, w = map(int, input().rstrip().split())
    edges[u].append((w, v))
# 다익스트라 알고리즘에 사용할 우선순위 큐
qu = PriorityQueue()
# 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
qu.put((0, s))
# 시작 노드와의 거리는 0으로 초기화
dists[s] = 0

while not qu.empty():
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    c_d, c_n = qu.get()
    # 방문노드 표시
    visits[c_n] = True
    # 현재 노드에 연결된 간선들을 확인하고 거리를 갱신
    for n_d, n_n in edges[c_n]:
        # 다음 노드가 방문한 노드라면, 건너뛰기
        if visits[n_n]: continue
        # 다음 노드까지의 거리가 현재 노드까지의 거리 + 다음 노드까지의 거리보다 작다면, 건너뛰기
        if dists[n_n] <= c_d + n_d: continue
        # 현재 노드와의 거리를 갱신
        dists[n_n] = c_d + n_d
        # 다음 노드를 큐에 삽입
        # 우선순위 큐이므로, 거리가 짧은 노드가 가장 먼저 나옴
        qu.put((dists[n_n], n_n))
        
# print(dists)
# 모든 노드로 가기 위한 최단 거리를 출력
for i, dist in enumerate(dists):
    if i == 0: continue
    if dist == 999_999_999:
        print("INF")
        continue
    print(dist)