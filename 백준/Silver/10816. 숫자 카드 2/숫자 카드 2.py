n = int(input())
cards = list(map(int, input().split()))
m= int(input())
finds = list(map(int, input().split()))

# 카드의 이름별로 갯수를 저장할 리스트
# 음수는 뒤쪽부터 저장됨
card_list = [0] * 20000001
# 카드의 이름별로 갯수를 저장
for card in cards:
    card_list[card] += 1
    
# 찾는 카드의 갯수를 출력
for card in finds:
    print(card_list[card], end=' ')