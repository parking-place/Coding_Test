n,m = map(int,input().split())
l = [*range(1,n+1)]
for i in range(m) :
    s,e,c = map(int,input().split())
    l[s-1:e] = l[c-1:e]+l[s-1:c-1]
print(*l)