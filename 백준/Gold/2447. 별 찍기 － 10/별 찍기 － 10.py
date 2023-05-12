from math import sqrt

sier = None

# 시에르핀스키 사각형을 그려주는 함수
def make_sierpinski(start, n):
    global sier
    # 사각형이 1이면 
    if n == 1: 
        # 해당 위치를 별로 채움
        sier[start[0]][start[1]] = '*'
        return
    
    # 작은 사각형의 가로세로 길이
    small_n = n//3
    # 작은 사각형의 시작점들을 저장할 리스트
    small_starts = []
    for i in range(3):
        for j in range(3):
            small_starts.append((start[0]+(i*small_n), start[1]+(j*small_n)))
            
    for small_start in small_starts:
        # 작은 사각형의 시작점이 구멍이 있어야 하는 곳이면(가운데)
        if small_start == (start[0]+small_n, start[1]+small_n):
            # 해당 사각형은 건너뜀
            continue
        # 작은 사각형의 시작점이 가운데가 아니면
        else:
            # 작은사각형에 대해 *을 채워줌
            make_sierpinski(small_start, small_n)
    return



n = int(input())

sier = [[ ' ' for _ in range(n)] for _ in range(n)]
    
start = (0,0)
make_sierpinski((0,0),n)

for i in range(n):
    for j in range(n):
        print(sier[i][j], end='')
    print()