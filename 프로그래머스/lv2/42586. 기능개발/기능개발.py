def solution(progresses, speeds):
    answer = []
    # list를 스택처럼 사용하기 위해 reverse
    progresses.reverse()
    speeds.reverse()
    
    while progresses:
        # 작업 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # 배포 카운트 초기화
        release_c = 0
        # 배포 가능한 작업이 있는지 확인
        while progresses:
            if progresses[-1] >= 100:
                progresses.pop()
                speeds.pop()
                release_c += 1
            else:
                break
        # 배포 가능한 작업이 있으면 배포
        if release_c > 0:
            answer.append(release_c)
    return answer