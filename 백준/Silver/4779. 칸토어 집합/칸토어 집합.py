# 재귀 형식으로 칸토어 집합의 -을 추가해주는 함수
def make_cantor(start, c_len):
    global cantor
    # 현재 칸토어집합의 길이가 1이면 -을 추가해준다.
    if c_len == 1:
        cantor[start] = '-'
        return 
    # 다음 칸토어 집합의 길이를 구해준다.
    n_len = c_len // 3
    for i in range(3):
        # 가운데는 패스해준다
        if i == 1:
            continue
        # 재귀적으로 칸토어 집합을 만들어준다.
        new_start = start + (n_len * i)
        make_cantor(new_start, n_len)

while True:
    try:
        n = int(input())
    except:
        break
    # 칸토어 길이 만큼의 공백을 만들어준다.
    c_len = 3 ** n
    cantor = [' ' for _ in range(c_len)]
    make_cantor(0, c_len)
    print(''.join(cantor))