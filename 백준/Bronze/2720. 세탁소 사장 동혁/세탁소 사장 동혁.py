n = int(input())
coin_d = { 0: 25, 1: 10, 2: 5, 3: 1 }
coins = [0,0,0,0]
for _ in range(n):
    changes = int(input())
    for k, v in coin_d.items():
        coins[k] = changes // v
        changes %= v
    print(*coins)
