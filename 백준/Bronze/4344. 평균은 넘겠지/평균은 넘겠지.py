n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    average = sum(l[1:])/l[0]
    count = 0
    for v in l[1:]:
        if v > average:
            count += 1
    print(f'{count/l[0]*100:.3f}%')
    