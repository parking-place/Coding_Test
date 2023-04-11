l = [3 for _ in range(2, 10)]
l[7-2], l[9-2] = 4, 4
a = [*range(65, 91)]
n = ''
for i in range(2, 10) :
    n += str(i) * l[i-2]

b = {chr(a[i]) : int(n[i])+1 for i in range(26)}
#print(*b.items(),sep='\n')

time = 0
for i in input() :
    time += b[i]
print(time)

