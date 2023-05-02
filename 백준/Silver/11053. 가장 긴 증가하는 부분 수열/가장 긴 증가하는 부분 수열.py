n = int(input())
# 입력받은 수열을 리스트에 저장
l = list(map(int, input().split()))
# dp 테이블 초기화
# 그 수부터 시작하는 가장 긴 증가하는 부분 수열의 길이를 저장
dp = {}

def long_array(i):
    # 만약 dp 테이블에 값이 있다면 그 값을 리턴
    if dp.get(i) != None:
        return dp[i]
    # 만약 dp 테이블에 값이 없다면 1을 저장
    else:
        dp[i] = 1
        
    # 만약 dp 테이블에 값이 없다면 재귀함수를 이용해 값을 구한 후 dp 테이블에 저장
    for j in range(i+1, n):
        # 현재 값과 재귀후 나온 값+1중 최댓값을 저장
        if l[i] < l[j]:
            dp[i] = max(long_array(j) + 1, dp[i])
    
    # dp 테이블에 저장된 값을 리턴
    return dp[i]

for i in range(n):
    long_array(i)
    
# print(l)
# print(dp)

result = sorted(dp.values(), key=lambda x:x, reverse=True)

print(result[0])