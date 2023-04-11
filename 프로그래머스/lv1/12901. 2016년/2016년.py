def solution(a, b):
    # 2016년은 금요일 부터 시작
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    # 2016년도 각 달의 일수
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    # 1월 1일 부터 a월 b일 까지의 일수
    d = sum(month[:a-1]) + b - 1

    # d일의 요일을 반환
    return days[d%7]