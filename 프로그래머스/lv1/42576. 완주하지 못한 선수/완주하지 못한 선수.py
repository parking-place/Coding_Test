def solution(participant, completion):
    # 이름순 정렬
    participant.sort()
    completion.sort()
    # 같은 번호끼리 비교시
    # 이름이 달라질 경우
    #  participant에 있는 이름이 완주 못함
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]