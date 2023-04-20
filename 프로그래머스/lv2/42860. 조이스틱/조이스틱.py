import re

# 알파벳별 A에서의 이동 횟수
al_c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 커서 이동횟수 구하는 함수.
# idx는 현재 커서 위치, name은 이름, default_drr은 기본 이동 방향
def get_mv_sum(name, default_drr='r'):
    
    # 오른쪽 노드로 이동하는 함수
    def move_r(r_idx, r_side_length):
        # 오른쪽 간선의 길이를 더함
        r_side_length += edge_lengths[r_idx]
        if r_idx == len(edge_lengths)-1: r_idx = -1  # 마지막 노드의 경우
        # 오른쪽 간선의 노드로 커서를 이동
        r_idx += 1
        # 오른쪽 간선의 노드를 방문했다고 표시
        is_completes[r_idx] = 0
        return r_idx, r_side_length
    
    # 왼쪽 노드로 이동하는 함수
    def move_l(l_idx, l_side_length):
        # 왼쪽 간선의 길이를 더함
        l_side_length += edge_lengths[l_idx-1]
        # 왼쪽 간선의 노드로 커서를 이동
        l_idx -= 1
        # 왼쪽 간선의 노드를 방문했다고 표시
        is_completes[l_idx] = 0
        return l_idx, l_side_length
    
    # 커서 이동횟수를 구하기 위한 타겟의 인덱스 리스트
    target_idxs = [i for i in range(len(name)) if name[i] != 'A' or i == 0]
    # 각 노드 사이의 거리를 구함
        # 노드 인덱스와 같은 인덱스는 오른쪽으로 이동하는 거리
        # 노드 인덱스-1과 같은 인덱스는 왼쪽으로 이동하는 거리
    edge_lengths = []
    for i in range(len(target_idxs)):
        j = i+1
        # 마지막 노드의 경우
        if j == len(target_idxs):
            j = 0
            l = len(name[target_idxs[i]:] + name[:target_idxs[j]])
            edge_lengths.append(l)
            break
        edge_lengths.append(abs(target_idxs[i] - target_idxs[j]))

    # 시작 노드에서 양 방향으로 얼마나 갔는지 저장하는 변수
    l_side_length = 0
    r_side_length = 0
    # 노드의 방문 여부 확인용 리스트 (0: 방문 안함, 1: 방문함)
    # 길이를 하나 더 길게한 이유는, 범위 밖의 인덱스를 방문했을 때 오류를 방지하기 위함
    is_completes = [1 for _ in range(len(target_idxs))]
    # 시작 노드는 방문했다고 표시
    is_completes[0]= 0
    # 좌우방향 시작 노드의 인덱스
    l_idx = 0
    r_idx = 0
    
    # 기본 이동 방향 저장
    last_dir = default_drr
    # 모두 방문할 때까지 반복
    while sum(is_completes):
        # 오른쪽 간선의 길이가 더 짧은 경우
        if edge_lengths[r_idx] < edge_lengths[l_idx-1]:
            r_idx, r_side_length = move_r(r_idx, r_side_length)
            last_dir = 'r'
        # 왼쪽 간선의 길이가 더 짧은 경우
        elif edge_lengths[r_idx] > edge_lengths[l_idx-1]:
            l_idx, l_side_length = move_l(l_idx, l_side_length)
            last_dir = 'l'
        # 양쪽 간선의 길이가 같은 경우, 이전에 이동한 방향으로 이동
        else:
            if last_dir == 'r':
                r_idx, r_side_length = move_r(r_idx, r_side_length)
                last_dir = 'r'
            else:
                l_idx, l_side_length = move_l(l_idx, l_side_length)
                last_dir = 'l'

    # 전체 길이는 오른쪽 간선의 길이 + 왼쪽 간선의 길이 + 더 짧은 간선의 길이
    # 더 짧은 간선을 더해주는 이유는 전체 길이를 최소화하기 위해서.
        # 더 긴 간선을 한번 더 돌아가는 것보다
        # 더 짧은 간선을 다시 돌아가는 것이 더 빠르기 때문.
        # 더 짧은 간선이 0이라면, 값의 변화가 없음
    total_length = l_side_length + r_side_length + min(l_side_length, r_side_length)
    
    # # 전체 길이와 비교
    # total_length = min(total_length, len(name)-1)
    
    # 한방향으로만 돌때의 길이를 구함
    del_l_A = len(re.sub(r'^A+', '', name))
    del_r_A = len(re.sub(r'A+$', '', name))-1
    # 모두 A인 경우가 있을 수 있으므로, 0보다 작은 값이 나오면 0으로 바꿔줌
    one_side = max( 0 , min(del_l_A, del_r_A))
    
    # 전체 길이와 한방향으로만 돌때의 길이 비교
    total_length = min(total_length, one_side)
    
    return total_length

def solution(name):
    # 이름의 알파벳 이동 횟수들의 합
    al_sum = sum([al_c[ord(al) - 65] for al in name])
    # 이름에서의 커서 이동횟수
    mv_sum = 0
    
    # 커서 이동횟수 구하기
    # 기본 이동방향이 오른쪽인지 왼쪽인지에 따라 가끔 오류가 발생할 수 있음
    # 둘 모두 구해주고, 더 작은 값을 반환
    mv_sum = min(get_mv_sum(name), get_mv_sum(name, 'l'))
    
    # print(f'al_sum : {al_sum}, mv_sum : {mv_sum}')
    # 커서이동횟수 + 알파벳이동횟수
    answer = al_sum + mv_sum
    return answer