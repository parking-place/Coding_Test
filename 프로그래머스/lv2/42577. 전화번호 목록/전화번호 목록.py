def solution(phone_book):
    answer = True
    # 딕셔너리 생성
    phone_dict = {}
    # 길이 순 정렬 -> 짧은 전화번호부터 딕셔너리에 저장 위함
    phone_book.sort(key=lambda x: len(x))
    # 전화번호부의 전화번호를 하나씩 처리
    for phone in phone_book:
        # 1 ~ 번호 길이까지 반복
        for i in range(1, len(phone)+1):
            # print(f'check {phone} in {phone[:i]}')
            # 번호 길이가 끝까지 반복했을 경우
            if i == len(phone):
                # print(f'add {phone} to dict')
                # 중복된 번호는 없으므로 키를 생성
                phone_dict[phone] = False
                continue
            # 번호를 i개만큼 자른 것이 딕셔너리에 있을 경우
            try:
                # 접두어인 번호가 있으므로 False반환
                check = phone_dict[phone[:i]]
                return False
            except:
                # 접두어인 번호가 없으므로 다음 번호로 넘어감
                continue

    return answer