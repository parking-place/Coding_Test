n = int(input())

for i in range(n) :
    a = list(map(int, input().split(' ')))
    print(f'{sum(a)}')