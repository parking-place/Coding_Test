n = int(input())
# 각 노드에 연결된 노드 정보를 담는 리스트
graph = [[] for _ in range(n+1)]
# 각 노드의 부모 노드를 담는 리스트
parent = [0] * (n+1)
# 루트 노드는 1이므로 표시
parent[1] = -1
# DFS에 사용할 스택
stack = [1]

# DFS로 부모 노드를 채워넣는 함수
def fill_parent():
    global parent, graph
    while stack:
        node = stack.pop()
        # 노드와 연결된 간선들을 가져옴
        edges = graph[node]
        # 부모 노드를 아직 못 찾은 경우
        for child_node in edges:
            if parent[child_node] == 0:
                parent[child_node] = node   # 부모 노드를 입력
                stack.append(child_node)    # 자식 노드를 스택에 추가

# 모든 간선 정보 입력받고 그래프에 연결
# 양방향으로 연결
for _ in range(n-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 루트 노드부터 시작해서 부모 노드를 채워넣음
fill_parent()

# 부모 노드 출력
for i in range(2, n+1):
    print(parent[i])