n=list(map(int,input().split()))
for i in range(6):
 print([1,1,2,2,2,8][i]-n[i],end=' ')