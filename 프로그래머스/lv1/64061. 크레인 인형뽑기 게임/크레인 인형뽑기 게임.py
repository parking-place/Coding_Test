# 뽑은 인형을 담을 바구니를 저장할 전역 변수
basket = []
# 인형이 담긴 보드를 저장할 전역 변수
board = []
# 사라진 인형의 개수를 저장할 전역 변수
count = 0

# 인혈을 받아서 바구니에 담는 함수
def put_in_basket(doll):
    global basket
    global count
    
    if len(basket) >= 1 :   # 바구니의 길이가 1 이상일 경우
        if basket[-1] == doll:  # 바구니의 마지막 인형과 받은 인형이 같은지 확인
            basket.pop()        # 같으면 바구니의 마지막 인형을 빼냄
            count += 2          # 사라진 인형의 개수를 2개 늘림
            return 
    
    # 바구니에 인형을 담음
    basket.append(doll)

# 인형을 뽑는 함수
def doll_drawing(m):
    global board
    for i in range(len(board)): # 배열의 맨 윗줄부터 탐색
        if board[i][m] != 0:        # 인형이 있는 경우
            doll = board[i][m]      # 인형을 뽑음
            board[i][m] = 0         # 인형이 있던 자리를 0으로 바꿈
            put_in_basket(doll)     # 인형을 바구니에 담음
            break

# 보드를 전역 변수로 저장
def set_board(_board):
    global board
    board = _board

def solution(board, moves):
    global count
    set_board(board)
    for move in moves:
        doll_drawing(move-1)
    return count