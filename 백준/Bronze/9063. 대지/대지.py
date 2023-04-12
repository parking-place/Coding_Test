n = int(input())

# 포인트 리스트
# point_l 를 굳이 만들지 않고 x_l, y_l를 만들어도 됨
x_l, y_l = [], []
for _ in range(n):
    x, y = list(map(int, input().split()))
    x_l.append(x)
    y_l.append(y)
    
# x, y 좌표중 최대, 최소값을 구함
e, w, n, s = max(x_l), min(x_l), max(y_l), min(y_l)

# 넓이를 구함 (동서 거리 * 남북 거리)
print((e-w)*(n-s))