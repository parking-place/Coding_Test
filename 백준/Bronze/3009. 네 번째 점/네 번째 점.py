p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

# x, y 좌표를 각각 리스트로 만듬
x_l = [p1[0], p2[0], p3[0]]
y_l = [p1[1], p2[1], p3[1]]

# x, y 좌표중 하나만 나오는 값을 찾음
x_result =  [ v for v in x_l if x_l.count(v) == 1 ]
y_result =  [ v for v in y_l if y_l.count(v) == 1 ]

print(x_result[0], y_result[0])
