import sys as s
n = int(s.stdin.readline().rstrip())
for i in range(n) :
    a, b = map(int, s.stdin.readline().rstrip().split(' '))
    print(a+b)