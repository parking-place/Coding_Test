from collections import deque # 큐를 사용하기 위해 deque를 import

n = int(input())  # 카드의 갯수를 입력받음
# 카드를 저장할 오름차순의 큐 생성
card_qu = deque(list(range(1, n+1)))
while len(card_qu) != 1:    # 카드가 한 장 남을 때까지 반복
    card_qu.popleft()                  # 맨 위의 카드를 버림
    card_qu.append(card_qu.popleft())  # 맨 위의 카드를 맨 아래로 옮김
print(card_qu[0])   # 남은 카드 출력