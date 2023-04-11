n, x = map(int, input().split(' '))
l = list(map(int, input().split(' ')))
l = [v for v in l if v < x]
for i in l :
    print(i, end=' ')