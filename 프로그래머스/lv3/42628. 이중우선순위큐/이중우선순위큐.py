import heapq
import re
# 'I 숫자' 또는 'D 숫자' 형식의 문자열을 정규식으로 표현
p = r'(I|D) (-?\d+)' # 'I' 또는 'D' + 공백 + 숫자 1개 이상
p = re.compile(p)
# 'I 숫자' 또는 'D 숫자' 형식의 문자열을 처리하는 함수 -> 딕셔너리와 람다식을 이용
cmnd = {
    'I' : lambda x, qu : heapq.heappush(qu, x),
    'D' : lambda x, qu : heapq.heappop(qu) if x == -1 else qu.pop(qu.index(max(qu)))
}

def solution(operations):
    # 우선순위 큐
    h_qu = []
    # 문자열을 처리
    for oper in operations:
        # 명령어와 숫자를 분리
        m = p.match(oper)
        c, n = m.group(1), int(m.group(2))
        # 삭제 명령인데 큐가 비어있으면 무시
        if c == 'D' and len(h_qu) == 0: continue
        # 명령어에 따라 처리
        cmnd[c](n, h_qu)

    # 결과 처리
    if len(h_qu) == 0:
        answer = [0, 0]
    elif len(h_qu) == 1:
        answer = [h_qu[0], h_qu[0]]
    else:
        answer = [max(h_qu), h_qu[0]]
    
    return answer