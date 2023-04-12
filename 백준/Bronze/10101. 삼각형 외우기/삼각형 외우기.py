a1 = int(input())
a2 = int(input())
a3 = int(input())

# 세 각의 합이 180
if a1 + a2 + a3 == 180:
    # 세 각이 모두 60
    if a1 == a2 and a2 == a3 and a3 == 60:
        print('Equilateral')
    # 두 각이 같은 경우
    elif a1 == a2 or a2 == a3 or a3 == a1:
        print('Isosceles')
    # 세 각이 모두 다른 경우
    else:
        print('Scalene')
# 세 각의 합이 180이 아닌 경우
else:
    print('Error')