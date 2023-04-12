def is_palindrome(s : str) -> 0 or 1 :
    """
    어떠한 수를 거꾸로 읽어도 똑같은 문자열을 팰린드롬(palindrome)이라고 한다.
    
    Args:
        num (type{str}): 펠린드롬인지 확인 할 문자

    Returns:
        0 or 1: 팰린드롬이면 1, 아니면 0
    """
    result = 1
    
    # str[]을 이용해 더 짧고 가독성이 좋게 가능
    if s != s[::-1]:
        result = 0

    return result

s = input()
print(is_palindrome(s))