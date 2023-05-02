# 동전 종류
coins = [500, 100, 50, 10, 5, 1]
# 받은 돈을 입력받고 거스름돈을 계산한다.
money = 1000 - int(input())
# 거스름돈의 개수를 저장할 변수
count = 0
for coin in coins:
    # 남은 돈을 현재의 돈전으로 나눈 몫과 나머지를 구한다.
    c, m = divmod(money, coin)
    # 거스름돈의 개수를 더한다.
    count += c
    # 나머지를 다시 거스름돈으로 계산한다.
    money = m

print(count)