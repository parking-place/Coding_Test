n = int(input())
cards = list(map(int, input().split()))
m= int(input())
finds = list(map(int, input().split()))

card_dict = {}
# 카드의 이름별로 갯수를 저장
for card in cards:
    try:
        card_dict[card] += 1
    except:
        card_dict[card] = 1
# 찾는 카드의 갯수를 출력
for card in finds:
    try:
        print(card_dict[card], end=' ')
    except:
        print(0, end=' ')