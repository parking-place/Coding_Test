# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

n = int(input())

# 코드1 시행 횟수
print(n*(n-1)//2)
# 최대차수 n^2
print(2)