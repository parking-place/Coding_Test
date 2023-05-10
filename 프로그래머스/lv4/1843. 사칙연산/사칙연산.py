# 모든 각각원소의 차를 구하기위해 2차원 배열로 변환, 벡터연산해주는 함수
def plus(a :list, b :list):
    max_ = a[-1] + b[-1] # a의 최댓값과 b의 최댓값을 더함
    min_ = a[0] + b[0]   # a의 최솟값과 b의 최솟값을 더함
    return [min_, max_]
def minus(a :list, b :list):
    max_ = a[-1] - b[0]  # a의 최댓값에서 b의 최솟값을 뺌
    min_ = a[0] - b[-1]  # a의 최솟값에서 b의 최댓값을 뺌
    return [min_, max_]
oper = {'+':plus, '-':minus}
# 각 부분 집합들이 가능한 결과들을 리스트로 저장할 딕셔너리
# key : s_idx,e_idx
# value : [min, max]
dict_ = None
# 전역으로 사용할 수 있도록 함수 밖에서 선언
nums = None
ops = None

def calcul(s_idx, e_idx):
    global dict_, nums, ops
    # key로 사용하기 위해 리스트를 문자열로 변환
    str_arr = str(s_idx) + ',' + str(e_idx)
    # 이미 계산한 부분집합이면 그 값을 반환
    if dict_.get(str_arr) != None:
        return dict_[str_arr]
    # 계산할 연산자가 없으면 그대로 반환
    if s_idx == e_idx or s_idx == len(nums):
        dict_[str_arr] = [nums[s_idx]]
        return dict_[str_arr]
    # 계산할 연산자가 1개이면 그대로 계산후 반환
    if s_idx + 1 == e_idx:
        if ops[s_idx] == '+':
            dict_[str_arr] = [nums[s_idx]+nums[e_idx]]
        else:
            dict_[str_arr] = [nums[s_idx]-nums[e_idx]]
        return dict_[str_arr]
    # 계산한 적 없는 부분집합이면 결과를 저장 리스트 생성-초기화
    dict_[str_arr] = [999_999_999, -999_999_999]
    # 모든 연산자가 +인 경우-> 결합법칙으로 모든 경우의 값이 같음.
    if '-' not in ops[s_idx:e_idx]:
        dict_[str_arr] = [sum(nums[s_idx:e_idx+1])]
        return dict_[str_arr]
    # 각 연산자를 기준으로 왼쪽과 오른쪽으로 나누어 가능한 결과들을 구함.
    # 각 결과들끼리 연산자를 적용하여 가능한 결과들을 구함.
    for i in range(s_idx, e_idx):
        # 왼쪽, 오른쪽 각각의 최저값과 최대값을 구함.
        left = calcul(s_idx, i)
        right = calcul(i+1, e_idx)
        # 연산자를 적용한 결과를 구함.
        r = oper[ops[i]](left, right)
        # 구한 결과를 저장
        dict_[str_arr][0] = min(dict_[str_arr][0], r[0])
        dict_[str_arr][-1] = max(dict_[str_arr][-1], r[-1])
    return dict_[str_arr]

def solution(arr):
    global dict_, nums, ops
    dict_ = {}
    # 숫자열과 연산자를 분리
    nums, ops = arr[::2], arr[1::2]
    # 수열을 모두 int형으로 변환
    nums = list(map(int, nums))
    # arr이 가능한 모든 결과들을 구하고 그 중 최댓값을 반환
    return calcul(0, len(nums)-1)[-1]