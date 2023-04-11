while True :
    n = list(map(int, input().split(' ')))
    if sum(n) == 0 :
        break
    print(sum(n))