import sys
from queue import PriorityQueue
# 백준 입력오류로 인한 입력 방식 변경
input = sys.stdin.readline
# 다익스트라 알고리즘에 사용할 우선순위 큐
qu = PriorityQueue()
# 도시의 개수, 버스의 개수 입력받기
city_c = int(input().rstrip())
bus_c = int(input().rstrip())
# 시작 도시와 도착 도시를 연결하는 노선에 대한 정보를 담을 리스트
edges = [ PriorityQueue() for _ in range(city_c + 1)]
# 모든 간선 정보 입력받기 -> 우선순위 큐로 입력받기
for _ in range(bus_c):
    s, e, m = map(int, input().rstrip().split())
    edges[s].put((m, e))
# 모든 간선 우선순위큐를 일반 큐(이터러블)로 변경
for i in range(city_c + 1):
    edges[i] = edges[i].queue
# 출발 도시로 부터 각 도시까지의 최단 거리를 담을 리스트
dists = [999_999_999] * (city_c + 1)
# 방문여부를 체크할 리스트
visits = [False] * (city_c + 1)
# 출발 도시와 도착 도시 입력받기
s_c, e_c = map(int, input().rstrip().split())
# qu에 (금액, 도시번호) 형태로 삽입
qu.put((0, s_c))
# 출발도시의 거리는 0으로 초기화
dists[s_c] = 0

while not qu.empty():
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    c_money, c_city = qu.get()
    # 방문 노드 표시
    visits[c_city] = True
    # 현재 노드에 연결된 간선들을 확인하고 거리를 갱신
    for n_money, n_city in edges[c_city]:
        # 다음 노드가 방문한 노드라면, 건너뛰기
        if visits[n_city]: continue
        # 비교후 갱신 필요 없다면, 건너뛰기
        if dists[n_city] <= c_money + n_money: continue
        # 현재 노드와의 거리를 갱신
        dists[n_city] = c_money + n_money
        # 큐에 삽입
        qu.put((dists[n_city], n_city))

print(dists[e_c])