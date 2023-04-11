n = int(input())
i=1
while True:
    if n <= 0:
        i -= 1
        n += i
        if i % 2 == 0:
            print(f'{n}/{i-n+1}')
        else:
            print(f'{i-n+1}/{n}')
        break
    n -= i
    i += 1