n = int(input())
p = 2
for _ in range(n):
    p += p-1
print(p**2)