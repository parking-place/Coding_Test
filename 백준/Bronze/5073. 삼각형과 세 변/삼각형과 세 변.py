while True:
    s1, s2, s3 = map(int, input().split())
    
    # 0 0 0 이 입력되면 종료
    if s1 == 0 and s2 == 0 and s3 == 0:
        break
    
    # 가장 긴 변이 다른 두 변의 합보다 작아야 함
    if max(s1,s2,s3) < (s1+s2+s3-max(s1,s2,s3)):
        # 세 변의 길이가 모두 같은 경우
        if s1 == s2 and s2 == s3:
            print('Equilateral')
        # 두 변의 길이가 같은 경우
        elif s1 == s2 or s2 == s3 or s3 == s1:
            print('Isosceles')
        # 세 변의 길이가 모두 다른 경우
        else:
            print('Scalene')
    # 가장 긴 변이 다른 두 변의 합보다 큰 경우
    else:
        print('Invalid')