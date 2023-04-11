def solution(answers):
    answer_dict = {
        1: [1,2,3,4,5],
        2: [2,1,2,3,2,4,2,5],
        3: [3,3,1,1,2,2,4,4,5,5]
    }   
    score_dict = {
        1: 0,
        2: 0,
        3: 0
    }
    
    answer = []
    for i in range(len(answers)):
        for s in range(1, 4):
            if answer_dict[s][i%len(answer_dict[s])] == answers[i]:
                score_dict[s] += 1
    
    max_score = max(score_dict.values())
    for k, v in score_dict.items():
        if v == max_score:
            answer.append(k)
    
    answer.sort()
    
    return answer