from collections import deque

def solution(priorities, location):
    count = 0  # 출력된 문서의 개수를 저장할 변수
    n = len(priorities)
    # 큐에 문서의 인덱스와 우선순위를 저장
    print_qu = deque([ [i , priorities[i]] for i in range(n)])
    # 큐가 빌 때까지 반복
    while len(print_qu) != 0:
        # 큐에서 문서를 pop
        doc = print_qu.popleft()
        # 큐에 문서가 남아있을 경우, 뽑은 문서보다 우선순위가 높은 문서가 있는지 확인
        if len(print_qu) != 0: 
            if max(print_qu, key=lambda x: x[1])[1] > doc[1]:
                print_qu.append(doc)    # 큐의 맨 뒤에 뽑은 문서를 추가
                continue                # 다음 문서를 pop하기 위해 반복문의 처음으로 이동
        
        # 조건에 해당하지 않을 경우, 출력된 문서의 개수를 1 증가    
        count += 1
        
        if doc[0] == location:  # 뽑은 문서가 찾는 문서일 경우
            return count