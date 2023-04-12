# 시간 표시를 분으로 바꾸는 함수
def hhmm_to_minutes(hhmm):
    hh, mm = hhmm.split(':')
    return int(hh) * 60 + int(mm)

# 분을 시간 표시로 바꾸는 함수
def min_to_hhmm(minutes):
    hh = minutes // 60
    mm = minutes % 60
    return f'{hh:02d}:{mm:02d}'

def doing_homework(plans, debug_mode = False):
    # 가장 빠른 시작 시간
    time = hhmm_to_minutes(plans[0][1])
    proceeding ,completed, stopped = [], [], []
    
    while True:
        # 멈춘 과제, 진행중인 과제, 계획된 과제가 모두 없으면 종료
        if stopped == [] and proceeding == [] and plans == []:
            break
        
        debug_line = []
        debug_line.append(f'\n시간: {min_to_hhmm(time)} -> ')
        
        #과제 종료 시간이 되면 완료된 과제에 추가
        if proceeding != []:
            if int(proceeding[0][2]) == 0:
                debug_line.append(f'과제 {proceeding[0][0]} 완료 ')
                completed.append(proceeding.pop(0))
                
        # 진행중인 과제가 없을 경우 멈춘 과제가 있으면 진행중인 과제로 추가
        if proceeding == []:
            if stopped != []:
                debug_line.append(f'과제 {stopped[-1][0]} 재시작 {stopped[-1][2]}분 남음 ')
                proceeding.append(stopped.pop(-1))
        
        # 과제 시작 시간이 되면 진행중인 과제에 추가
        if plans != []:
            if time == hhmm_to_minutes(plans[0][1]):
                # 진행중이던 과제가 있으면 멈춘 과제에 추가
                if proceeding != []:
                    debug_line.append(f'과제 {proceeding[0][0]} 멈춤 {proceeding[-1][2]}분 남음 ')
                    stopped.append(proceeding.pop(0))
                debug_line.append(f'과제 {plans[0][0]} 시작 {plans[0][2]}분 남음 ')
                proceeding.append(plans.pop(0))
        
        # 시간 증가
        time += 1
        # 진행중인 과제의 남은 시간 감소
        if proceeding != []:
            proceeding[0][2] = int(proceeding[0][2]) - 1
        
        if len(debug_line) > 1 and debug_mode:
            print(*debug_line)
            
    return completed
        

def solution(plans, debug_mode = False):
    answer = []
    # 시작 시간이 빠른 순서대로 정렬
    plans.sort(key=lambda x: x[1])
    
    complete = doing_homework(plans, debug_mode)
    
    # 과제 이름만 추출
    answer = [ v[0] for v in complete ]
    
    return answer