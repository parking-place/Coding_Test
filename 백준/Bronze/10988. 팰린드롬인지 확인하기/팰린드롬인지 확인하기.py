def is_palindrome(s : str) -> 0 or 1 :
    """
    어떠한 수를 거꾸로 읽어도 똑같은 문자열을 팰린드롬(palindrome)이라고 한다.
    
    Args:
        num (type{str}): 펠린드롬인지 확인 할 문자

    Returns:
        0 or 1: 팰린드롬이면 1, 아니면 0
    """
    result = 1

    # 문자열의 절반만 반복
    for i in range(len(s)//2) :
        if s[i] != s[len(s)-i-1] :    # 앞뒤로 비교
            result = 0
            break

    return result

s = input()
print(is_palindrome(s))