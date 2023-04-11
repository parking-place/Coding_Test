while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break

    if a > b and a % b == 0:
        print('multiple')
        continue
    if b > a and b % a == 0:
        print('factor')
        continue
    print('neither')