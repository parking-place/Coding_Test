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
    """
    
    n_min = 2
    
    
    if from_is_prime :
        # 모든 수는 자신의 제곱근보다 큰 소인수를 가지지 못함
        n_max = int(num**0.5)+1
    else :
        # 어떤 수 보다 작은 소수를 구해두는 경우
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

n = int(input())
l = input()
l = l.split(' ')
l = [int(v) for v in l]

l = list(set(l))
n = len(l)

#l의 최대값까지의 소수 리스트를 만듬
eratosthenes_shecker(1000, from_is_prime=False)   

# 소수 개수
prime_count = 0
primes_set = set()

for v in l :
    if v in prime_num :
        primes_set.add(v)
        prime_count += 1
answer = str(len(primes_set))
print(answer)