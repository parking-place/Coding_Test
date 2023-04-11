def solution(s : str):
    result = True
    if not (len(s) == 4 or len(s) == 6):
        result = False
    
    if not(s.isdigit()):
        result = False
    
    return result