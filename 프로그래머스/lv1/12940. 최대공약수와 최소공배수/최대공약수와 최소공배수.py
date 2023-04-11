def solution(n, m):
    answer = []
    
    # 최대 공약수를 구해 answer에 추가
    # 거꾸로 돌면서 나누어 떨어지는 수를 찾아야
    # 최댓값만 찾을 수 있다.
    for i in range(min(n,m), 0, -1) :
        if n%i == 0 and m%i == 0 :
            answer.append(i)
            break
     
    # 최소 공배수를 구해 answer에 추가
    for i in range(max(n,m), n*m+1) :
        if i%n == 0 and i%m == 0 :
            answer.append(i)
            break
    
    return answer