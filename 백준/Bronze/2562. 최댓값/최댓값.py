l = []
for _ in range(9) :
    l.append(int(input()))
n = max(l)
print(f'{n}\n{l.index(n)+1}')