# 행, 열 입력받기
row, col = map(int, input().split())
# 보드 입력받기
full_bord= []

def check_bord(x, y):
    painted_count = 0
    for i in range(8):
        for j in range(8):
            # 해당 위치의 색이 다르면 칠해야하는 칸의 수를 증가
            # ^ = XOR 연산자, 둘이 다르면 1, 같으면 0
            if full_bord[x+i][y+j] ^ ((i + j) % 2):
                painted_count += 1
    # 칠해야하는 칸의 수를 반환 (반대의 경우 칠해야하는 칸의 수가 더 작을 수도 있음)
    return min(painted_count, 64 - painted_count)

for _ in range(row):
    line = input()
    # W는 0, B는 1로 변환
    l = [ 0 if s == 'W' else 1 for s in line]
    full_bord.append(l)

# 8x8 보드를 만들기 위해 확인해 봐야할 행, 열의 수
row -= 7
col -= 7
results =[]
for x in range(row):
    for y in range(col):
        result = check_bord(x, y)
        # 결과를 저장
        results.append(result)
# 최소값 출력
print(min(results))