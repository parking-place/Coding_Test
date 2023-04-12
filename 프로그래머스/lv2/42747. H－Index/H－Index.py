def solution(citations):
    answer = 0
    
    # 내림차순 정렬
    citations.sort(reverse=True)
    
    # print(citations)
    
    # h-index의 최대값
    max_h = 0
    
    for i, v in enumerate(citations):
        # i편 이상이 i번 이상 인용되어야 하므로,
        # i보다 v가(i번째 논문의 인용 횟수) 작으면,
        # h-index는 i+1이 됨 (+1은 i가 0부터 시작하기 때문)
        if i < v:
            max_h = i+1
    
    # h-index가 논문의 개수보다 크면 논문의 개수를 반환
    answer = min(max_h, len(citations))
        
    return answer