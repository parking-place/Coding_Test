from math import sqrt

sier = None

# 시에르핀스키 사각형에 구멍을 뚫는 함수
def make_sierpinski(start, n):
    global sier
    # 사각형이 1이면 더이상 구멍을 뚫지 않음
    if n == 1: return
    
    # 작은 사각형의 가로세로 길이
    small_n = n//3
    # 작은 사각형의 시작점들
    small_starts = []
    for i in range(3):
        for j in range(3):
            small_starts.append((start[0]+(i*small_n), start[1]+(j*small_n)))
            
    for small_start in small_starts:
        # 작은 사각형의 시작점이 구멍이 뚫려야하는 곳이면(가운데)
        if small_start == (start[0]+small_n, start[1]+small_n):
            # 작은 사각형의 시작점부터 작은 사각형의 가로세로 길이만큼
            # 구멍을 뚫음
            for i in range(small_start[0], small_start[0]+small_n):
                for j in range(small_start[1], small_start[1]+small_n):
                    sier[i][j] = ' '
        # 작은 사각형의 시작점이 가운데가 아니면
        else:
            # 작은사각형에 대해 다시 구멍을 뚫음
            make_sierpinski(small_start, small_n)
    return



n = int(input())

sier = [[ '*' for _ in range(n)] for _ in range(n)]
    
start = (0,0)
make_sierpinski((0,0),n)

for i in range(n):
    for j in range(n):
        print(sier[i][j], end='')
    print()