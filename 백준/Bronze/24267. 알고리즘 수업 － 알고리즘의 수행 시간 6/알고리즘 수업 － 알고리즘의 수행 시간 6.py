# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

n = int(input())

# 코드1 시행 횟수
print( ((n-2)*(n-1)*n)//6 )
# 최대차수 n^3 => (n-2)(n-1)n/6
print(3)