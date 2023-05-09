from collections import deque
rows = None
outlines = None
len_h = 0
len_w = 0
len_o = 0
# shiftrow 연산을 n번 수행하는 함수
def shiftrow(n):
    global rows, outlines
    # n이 행렬의 크기보다 클 경우, n을 행렬의 크기로 나눈 나머지를 구한다.
    n = n % len_h
    # n만큼 행렬의 행을 밀어준다.
    rows.rotate(n)
    outlines[0].rotate(n)
    outlines[1].rotate(n)
    
    # row_outlins_print(n, 'shiftrow')
    
# rotate 연산을 n번 수행하는 함수
def rotate(n):
    global rows, outlines
    # n이 테두리의 길이보다 클 경우, n을 테두리의 길이로 나눈 나머지를 구한다.
    n = n % len_o
    # print(rows[0], outlines[1], rows[-1], outlines[0])
    # 테두리를 n칸씩 밀어준다.
    for _ in range(n):
        try:
            # 첫 행 -> 마지막 열.
            outlines[1].appendleft(rows[0].pop())
            # 마지막 열 -> 마지막 행.
            rows[-1].append(outlines[1].pop())
            # 마지막 행 -> 첫 열.
            outlines[0].append(rows[-1].popleft())
            # 첫 열 -> 첫 행.
            rows[0].appendleft(outlines[0].popleft())
        except:
            # 열의 갯수가 2개라 rows[0]이 비어있을 경우
            # 열끼리 바꿔준다.
            outlines[0].append(outlines[1].pop())
            outlines[1].appendleft(outlines[0].popleft())
        
    # row_outlins_print(n, 'rotate')
    # print(rows[0], outlines[1], rows[-1], outlines[0])

def solution(rc, operations):
    # matrix_print(rc)
    global len_h, len_w, len_o, rows, outlines
    len_h, len_w = len(rc), len(rc[0])  # 행렬의 세로, 가로 길이
    len_o = len_h*2 + len_w*2 - 4       # 테두리의 길이
    
    # 양 끝 원소를 제외한 행렬을 deque로 만든다.
    rows = deque(deque(r[1:-1]) for r in rc)
    # 행렬의 첫열, 마지막열을 deque로 만든다.
    outlines = [
                deque(r[0] for r in rc), # 첫 열
                deque(r[-1] for r in rc) # 마지막 열
                ]
    # 명령을 딕셔너리로 만든다.
    oper = {'Rotate': rotate, 'ShiftRow': shiftrow}
    # 연산을 수행한다.
    op_count = 0
    for i, op in enumerate(operations):
        # 마지막 연산이면 연산을 수행한다.
        if i == len(operations) - 1:
            op_count += 1
            oper[op](op_count)
            break
        # 다음 연산이 연속된 연산이면 연산 횟수를 늘려주고, 아니면 연산을 수행한다.
        if op == operations[i+1]:
            op_count += 1
        else:
            op_count += 1
            oper[op](op_count)
            op_count = 0    # 연산한뒤 연산횟수를 초기화한다.
            
    # rows, outlines를 다시 행렬로 만든다.
    answer = [[outlines[0][i]] + list(rows[i]) + [outlines[1][i]] for i in range(len_h)]
    # matrix_print(answer)
    return answer