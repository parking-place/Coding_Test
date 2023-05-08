import heapq

def solution(scoville, K):
    answer = 0
    # 음식들을 우선순위 큐로 만들기 -> 낮은 스코빌 지수 순으로 정렬됨
    qu = []
    for scov in scoville:
        heapq.heappush(qu, scov)
    # 남은 음식이 1개보다 적을 때까지 반복
    while len(qu) > 1:
        # 스코빌 지수가 낮은 음식을 가져옴
        h_scv = heapq.heappop(qu)
        n_scv = heapq.heappop(qu)
        # 스코빌 지수가 낮은 음식이 K보다 크거나 같으면 종료
        if h_scv >= K: break
        # 스코빌 지수를 계산후 큐에 넣음(우선순위 큐이므로 자동으로 정렬됨)
        heapq.heappush(qu, h_scv + n_scv * 2)
        # 음식을 섞은 횟수 증가
        answer += 1
    # 남은 음식이 1개이고 스코빌 지수가 K보다 작으면 -1 반환
    if len(qu) == 1:
        if K > heapq.heappop(qu):
            answer = -1
    # 섞은 횟수 반환
    return answer