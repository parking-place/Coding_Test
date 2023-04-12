# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
# f(n) = a1n + a0, 양의 정수 c, n0 가 주어질 경우 O(n) 정의를 만족하는지 알아보자.
# 
# -> g(n) = n
# 
# f(n) <= c * g(n)
# f(n) = a1n + a0 <= c * g(n) = c * n
# a1n + a0 <= cn
# a1n - cn + a0 <= 0
# (a1 - c)n + a0 <= 0
#
# (a1 - c)n + a0 = f_(n) 이라고 할때,
#
# 1. (a1 - c) > 0,                  (a1 > c)
#       1-1. f_(n) <= 0 이 항상 불만족 
# 
# 2. (a1 - c) == 0,                 (a1 == c)
#       2-1. a0 > 0 이면, f_(n) <= 0 이 항상 불만족
#       2-2. a0 == 0 이면, f_(n) = 0 이 항상 만족   ( f(n) = c*n )
#       2-3. a0 < 0 이면, f_(n) < 0 이 항상 만족    ( f(n) < c*n )
#
# 3. (a1 - c) < 0 이면, n0에서       (a1 < c)
#       3-1. f_(n0) > 0 이면, 불만족
#       3-2. f_(n0) <= 0 이면, 만족

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
# f_(n) = (a1 - c)*n + a0 
f_ = lambda x: (a1 - c)*x + a0

is_right = 0
# 2-2번, 2-3번 조건
if a1 == c and a0 <= 0:
    is_right = 1
# 3-2번 조건
elif a1 < c and f_(n0) <= 0:
    is_right = 1

print(is_right)