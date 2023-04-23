from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 트럭 리스트를 큐로 변환
    truck_weights = deque(truck_weights)
    # 다리를 큐로 구현 (길이만큼의 0으로 초기화)
    bridg = deque([0] * bridge_length)
    # 현재 다리 하중
    now_weight = 0
    
    # 모든 트럭이 지나갈 때까지 반복
    while truck_weights:
        # 시간
        answer += 1
        
        # 현재 다리하중에서 나간 무게를 제거
        # 0이 나오면 나간 트럭이 없는것.
        now_weight -= bridg.popleft()
        
        # 현재 다리 하중 + 다음트럭 <= 다리가 견딜 수 있는 무게
        if now_weight + truck_weights[0] <= weight: 
            truck = truck_weights.popleft()
            # 현재 다리 하중에 트럭 무게 더함
            now_weight += truck
            # 다리에 트럭 추가
            bridg.append(truck)
        # 현재 다리하중 + 다음트럭 > 다리가 견딜 수 있는 무게
        else:
            # 다리에 0 추가
            bridg.append(0)
        
        # print(bridg)
    
    # 마지막 트럭이 다리를 지나는 시간을 더해줌
    answer += bridge_length 
    
    return answer