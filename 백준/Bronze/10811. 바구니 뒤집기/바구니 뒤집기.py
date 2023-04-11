f=lambda:map(int,input().split())
n,m=f()
b=[*range(1,n+1)]
for _ in range(m):
    i,j=f()
    b[i-1:j]=b[i-1:j][::-1]
print(*b)