def count_one_to_x(n, x):
    count = 0
    # x가 0이라면, 0을 반환
    if x == 0: return 0
        
    # 5**(n-1) -> n-1차 유사 칸토어 비트열의 자릿수
    # n차 유사 칸토어 비트열은 4개의 n-1차 유사 칸토어 비트열과 0들로 이루어져 있다.
    # 몫 = x이전까지 n-1차 비트열의 개수
    # 나머지 = n-1차 내에서의 x의 위치
    q, r = divmod(x, 5**(n-1))
    
    # 몫이 0이라면, n-1차 안에서 다시 구해야함.
    if q == 0: return count_one_to_x(n-1, x)
    
    # n_m1 = n-1차 비트열 하나에서 1의 갯수
    n_m1 = 4 ** ( n - 1 )
    # n-1 비트열에서 1의 갯수 * n-1 비트열의 갯수
    count = n_m1 * q
    # 몫이 3보다 크다면 0만 있는 비트열이 포함되어 있으므로, n-1 비트열의 1 갯수만큼 빼준다.
    if q >= 3: count -= n_m1
    
    # 만일 몫이 2라면,
        # x는 n-1차 비트열중 0이 있는 위치에 위치하므로, 더 구할 필요는 없음.
    # 만일 나머지가 0이라면,
        # 해당 x가 n-1차 비트열의 끝에 위치한다는 뜻이므로, 더 구할 필요는 없음.
    if q == 2 or r == 0: return count
    
    # 현재까지 구한 1의 갯수 + n-1차 비트열에서 x의 위치까지의 1의 갯수
    return count + count_one_to_x(n-1, r)


def solution(n, l, r):
    
    answer = count_one_to_x(n, r) - count_one_to_x(n, l-1)
    
    return answer