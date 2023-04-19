def solution(A,B):
    # A와 B를 오름차순, 내림차순으로 정렬
    # 서로 작은수와 큰수를 곱하면 최솟값이 됨
    A.sort()
    B.sort(reverse=True)
    
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer