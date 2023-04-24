import sys

# 팩토리얼을 저장할 딕셔너리
factorials = [1,1,2,6,24,120]

while True:
    # 입력을 문자열로 저장
    num_base_fac = sys.stdin.readline().rstrip()
    # 입력이 0이면 종료
    if num_base_fac == '0':
        break
    # 10진수를 저장할 변수
    base_10 = 0
    # 문자열을 역순으로 읽어가면서 팩토리얼을 곱해 10진수로 변환
    for i in range(1, len(num_base_fac)+1):
        base_10 += int(num_base_fac[-i]) * factorials[i]
    
    print(base_10)