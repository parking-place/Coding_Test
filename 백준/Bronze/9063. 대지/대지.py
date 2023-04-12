n = int(input())

# 포인트 리스트
point_l = []
for _ in range(n):
    point_l.append(list(map(int, input().split())))

# x, y 좌표를 각각 리스트로 만듬
x_l = [ p[0] for p in point_l ]
y_l = [ p[1] for p in point_l ]

# x, y 좌표중 최대, 최소값을 구함
e, w, n, s = max(x_l), min(x_l), max(y_l), min(y_l)

# 넓이를 구함 (동서 거리 * 남북 거리)
print((e-w)*(n-s))