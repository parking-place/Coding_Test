def solution(s : str):
    # s를 소문자로 바꿈
    s = s.lower()
    # s를 단어 단위로 나눔
    # 단어들을 한글자 단위의 리스트로 만듬
    words = [list(v) for v in s.split(' ')]
    # 새 단어 리스트 생성
    new_s = []
    for word in words:
        # 첫 글자가 알파벳이면 대문자로 바꿈
        if word == []:
            new_s.append('')
            continue
        if word[0].isalpha():
            word[0] = word[0].upper()
        # 새 단어 리스트에 추가
        new_s.append(''.join(word))
    # 새 단어 리스트를 공백으로 연결
    answer = ' '.join(new_s)
    return answer