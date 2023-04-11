n, m = map(int, input().split())
l1 = []
l2 = []
for _ in range(n):
    l1.append(list(map(int, input().split())))
for _ in range(n):
    l2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        l1[i][j] += l2[i][j]
        print(l1[i][j], end=' ')
    print()