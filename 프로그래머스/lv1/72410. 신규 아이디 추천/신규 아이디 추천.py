import re

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환.
def step_1(_id):
    return _id.lower()

# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거.
def step_2(_id):
    return re.sub(r'[^a-z0-9-_.]', '', _id)    # 정규식을 사용하여 제거

# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환.
def step_3(_id):
    return re.sub(r'\.{2,}', '.', _id)

# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거.
def step_4(_id):
    return re.sub(r'^\.|\.$', '', _id)

# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입.
def step_5(_id):
    return 'a' if _id == '' else _id

# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거.
# 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거.
def step_6(_id):
    return _id[:15].rstrip('.') if len(_id) >= 16 else _id

# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복, 끝에 붙임.
def step_7(_id):
    if len(_id) <= 2:
        _id += _id[-1] * (3 - len(_id))
    return _id


def solution(new_id):
    # 모든 단계를 순서대로 실행
    steps = [step_1, step_2, step_3, step_4, step_5, step_6, step_7]
    for step in steps:
        new_id = step(new_id)
    return new_id