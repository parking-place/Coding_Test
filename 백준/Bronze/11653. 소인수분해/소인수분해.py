answer = ''

# 소수 리스트
prime_num = [2, 3, 5, 7]

# 에라토스테네스의 체
def eratosthenes_shecker(num : int, *, from_is_prime : bool = True) -> None:
    """
    에라토스테네스의 체를 이용하여 소수 리스트를 만드는 함수
    Args:
        num (type[int]): 이 수의 제곱근보다 작은 모든 소수를 구함
        
        from_is_prime (bool, optional): num이 is_prime 함수에서 호출되었는지 확인. Defaults to True.
                                        아닐 경우, num보다 작은 모든 소수를 구함
    """
    n_min = 2
    
    # is_prime 함수에서 호출되었을 경우
    if from_is_prime :
        # 모든 수는 자신의 제곱근보다 큰 소인수는 검사하지 않아도 됨
        n_max = int(num**0.5)+1
    # is_prime 함수에서 호출되지 않았으며, 어떤 수 보다 작은 모든 소수를 구하는 경우
    else :
        n_max = num

    # 받은 값이 체 범위내에 있을 경우
    if num <= prime_num[-1] :
        return

    # 소수 리스트에 이후 숫자들을 추가
    prime_num.extend(list(range(prime_num[-1]+1,n_max)))
    
    # print(prime_num)
    
    # '소수판별 체' 알고리즘
    for i in prime_num:
        for j in prime_num:
            if i!=j and 0==(j%i):
                prime_num.remove(j)
    return

# 소수 판별
def is_prime(num : int) -> bool :
    """
    소수 판별 함수
    Args:
        num (type[int]): 소수인지 확인 할 숫자

    Returns:
        bool: 소수이면 True, 아니면 False
    """
    result = True
    
    # 소수 리스트에 있는지 먼저 확인
    if num in prime_num :
        return result

    # 소수 리스트 범위 내에 없으면 에라토스테네스의 체를 이용하여 소수 리스트를 만듬
    if num > prime_num[-1] :
        eratosthenes_shecker(num)
    
    # 소수 리스트중 나누어 떨어지는 수가 있으면 소수가 아님
    for v in prime_num :
        if num % v == 0 :
            result = False
    
    return result

# n의 소인수 구하기
n = int(input())
prime_factors = []
if n == 1:
    pass
else:    
    # 소수 리스트에 N 제곱근 이하의 소수를 추가
    eratosthenes_shecker(n)
    
    # 소수리스트를 이용하여 소인수 구하기
    for prime in prime_num :
        while n % prime == 0 :
            n //= prime
            prime_factors.append(prime)
        if n != 1 and is_prime(n):
            prime_factors.append(n)
            break

prime_factors.sort()

for v in prime_factors :
    print(v)