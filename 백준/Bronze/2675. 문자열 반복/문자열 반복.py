n=int(input())
for _ in range(n):
 r,a=input().split()
 print(*[v*int(r)for v in a],sep='')