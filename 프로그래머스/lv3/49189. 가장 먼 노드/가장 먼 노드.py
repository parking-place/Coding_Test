from collections import deque

def solution(n, edges):
    # BFS를 위한 큐 생성
    qu = deque()
    # 각 노드의 1부터의 거리를 저장하는 리스트, 방문여부를 확인하기 위해 -1로 초기화
    distances = [-1] * (n+1)
    # 각 노드의 연결된 노드들을 저장하는 리스트
    nodes = [[] for _ in range(n+1)]
    
    # nodes = [[]] * (n+1)  -> 참조가 복사되어서 같은 리스트가 n+1개 생성됨
    
    # print(edges)
    # print(nodes)
    
    # 각 노드에 간선들을 저장
    for edge in edges:
        # print(edge)
        nodes[edge[0]].append(edge[1])
        nodes[edge[1]].append(edge[0])
        # print(nodes)
    
    # print(nodes)
    
    # 1번 노드를 큐에 삽입
    qu.append(1)
    # 1번 노드의 거리를 0으로 설정
    distances[1] = 0
    
    # 큐가 빌 때까지 반복
    while qu:
        # 큐에서 노드를 꺼냄
        node = qu.popleft()
        # 노드의 간선들을 확인
        for next_node in nodes[node]:
            # 방문하지 않은 노드인 경우, 혹은 현재 노드의 거리 + 1이 더 작은 경우
            if distances[next_node] == -1 or distances[next_node] > distances[node] + 1:
                # 거리를 현재 노드의 거리 + 1로 설정
                distances[next_node] = distances[node] + 1
                # 큐에 삽입
                qu.append(next_node)
                
    # print(distances)
    
    # 최대 거리를 구함
    max_distance = max(distances)    
    # 최대 거리를 가진 노드의 수를 구함
    answer = distances.count(max_distance)
    
    return answer