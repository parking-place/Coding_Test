def solution(participant, completion):
    # 딕셔너리 생성
    dict_ = {}
    # 이름 key, value = 총 명수
    for name in participant:
        dict_[name] = dict_.get(name, 0) + 1
    # 완주한 사람은 -1 -> 0이 되면 삭제
    for name in completion:
        dict_[name] -= 1
        if dict_[name] == 0:
            del dict_[name]
    # 남은 이름이 완주 못한 사람
    answer = list(dict_.keys())[0]
    
    return answer