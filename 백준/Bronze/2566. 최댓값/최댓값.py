l = []
for _ in range(9):
    l.append(list(map(int, input().split())))
max_l = [max(v) for v in l]
t_max = max(max_l)
i = max_l.index(t_max)
j = l[i].index(t_max)
print(t_max)
print(i+1,j+1)