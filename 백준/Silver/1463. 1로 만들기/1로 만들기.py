n = int(input())

# 동적계획법(메모이제이션)에 사용할 딕셔너리
# 키: 숫자, 값: 1로 만들기 위한 최소 연산 횟수
dp_dict = { 1:0, 2:1, 3:1 }
# 재귀함수를 이용해 1로 만들기
def make_one(x):
    # 만약 딕셔너리에 값이 있다면 그 값을 리턴
    if dp_dict.get(x) != None:
        return dp_dict[x]
    # 만약 딕셔너리에 값이 없다면 재귀함수를 이용해 값을 구한 후 딕셔너리에 저장
    # 3과 2에 모두 나누어 떨어질 경우-> 어느 방향이 더 빠른지 모르므로 둘 중 최솟값 +1 을 저장
    if x%3 == 0 and x%2 == 0:
        dp_dict[x] = min(make_one(x//3), make_one(x//2)) + 1
    # 3으로만 나누어 떨어질 경우, 3으로 나눈 값과 -1한뒤 확인할 값중 최솟값 +1 을 저장
    elif x%3 == 0:
        dp_dict[x] = min(make_one(x//3), make_one(x-1)) + 1
    # 2로만 나누어 떨어질 경우, 2로 나눈 값과 -1한뒤 확인할 값중 최솟값 +1 을 저장
    elif x%2 == 0:
        dp_dict[x] = min(make_one(x//2), make_one(x-1)) + 1
    # 3과 2로 나누어 떨어지지 않을 경우, -1한 값을 찾아 +1 을 값으로 저장
    else:
        dp_dict[x] = make_one(x-1) + 1
    
    return dp_dict[x]

result = make_one(n)
print(result)