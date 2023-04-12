test = 1

def solution(n, lost, reserve):
    
    global test
    print(f'테스트 케이스 {test}')
    test += 1
    
    answer = 0
    
    #혹시 모르니까 정렬
    lost.sort()
    reserve.sort()
    
    # 전체학생중 잃어버린 학생과 여벌 옷이 있는 학생을
    # 각각의 리스트에서 True로 표시 ->  옷을 여러개 가져올 수 있을거같아
    # 가지고 온 옷의 갯수를 표시로 변경
    lost_ = [0 for _ in range(n+1)]
    for v in lost:
        lost_[v] -= 1
            
    reserve_ = [0 for _ in range(n+1)]
    for v in reserve:
        reserve_[v] += 1
            
    print(f'학생 수 : {n}')
    print(f'잃어버린 학생 \t\t: {lost_[1:]}')
    print(f'여벌 옷이 있는 학생 \t: {reserve_[1:]}')
    
    for i in range(1, n+1):
        # 잃어버린 사람 == 여벌 옷이 있는 사람
        if lost_[i] == -1 and reserve_[i] >= 1:
            lost_[i] += 1
            reserve_[i] -= 1
    
    for i in range(1, n+1):
        # 잃어버린 사람 and 여벌 옷이 있는 사람 - 1
        if lost_[i] == -1 and reserve_[i-1] >= 1:
            lost_[i] += 1
            reserve_[i-1] -= 1
        # 잃어버린 사람 and 여벌 옷이 있는 사람 + 1
        elif i < n:
            if lost_[i] == -1 and reserve_[i+1] >= 1:
                lost_[i] += 1
                reserve_[i+1] -= 1
    
    print(f'여전히 옷이 없는 학생 : {sum(lost_[1:])}')
    # 아직 옷이없는 사람 수
    # 부족한 옷은 -1로 표시되어 있으므로
    # sum(lost_)를 통해 부족한 옷의 수를 구함
    answer = n + sum(lost_)
    
    return answer