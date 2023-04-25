from collections import deque

def bfs(start):
    # 큐 생성
    qu = deque()
    # 시작 노드를 큐에 넣고 방문 표시
    qu.append(start)
    bfs_visits[start] = True
    # 큐가 빌 때까지 반복
    while qu:
        # 큐에서 노드를 하나 꺼내고 출력
        c_node = qu.popleft()
        print(c_node, end=' ')
        # 해당 노드와 연결된 노드 중 방문하지 않은 노드를 큐에 넣고 방문 표시
        for n_node in nodes[c_node]:
            if bfs_visits[n_node]:
                continue
            qu.append(n_node)
            bfs_visits[n_node] = True

def dfs(start):
    # 스택 생성
    stack = []
    # 시작 노드를 스택에 넣기
    stack.append(start)
    # 스택이 빌 때까지 반복
    while stack:
        # 스택에서 노드를 하나 꺼냄
        c_node = stack.pop()
        # 방문한 노드라면 다음 노드로 넘어감
        if dfs_visits[c_node]:
            continue
        # 방문하지 않은 노드라면 방문 표시, 출력
        dfs_visits[c_node] = True
        print(c_node, end=' ')
        # 작은수부터 스택에 넣기위한 임시 스택
        temp_stack = []
        # 해당 노드와 연결된 노드 중 방문하지 않은 노드를 임시 스택에 넣고 방문 표시
        # 임시스택에 작은수부터 들어감
        for n_node in nodes[c_node]:
            if dfs_visits[n_node]:
                continue
            temp_stack.append(n_node)
        # 임시 스택에 있는 노드를 스택으로 옮김
        # 큰 수부터 스택에 들어감 -> 작은수부터 방문
        while temp_stack:
            stack.append(temp_stack.pop())

# 노드의 갯수, 간선의 갯수, 시작 노드
n, e, start = map(int, input().split())
# 노드에 연결된 노드 정보를 담는 리스트
nodes = [[] for _ in range(n+1)]
# 노드 방문 여부를 담는 리스트
dfs_visits = [False] * (n+1)
bfs_visits = [False] * (n+1)
# 노드에 간선 정보 입력
for _ in range(e):
    n1, n2 = map(int, input().split())
    nodes[n1].append(n2)
    nodes[n2].append(n1)
# 정점 번호가 작은 것을 먼저 방문해야하므로 정렬
for node in nodes:
    node.sort()
# dfs, bfs 실행
dfs(start)
print()
bfs(start)