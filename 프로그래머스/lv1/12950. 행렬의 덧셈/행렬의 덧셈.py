def solution(arr1, arr2):
    answer = [[]]
    
    # answer을 컴프리헨션으로 초기화
    # [ [0 for j in range(안쪽 리스트 길이))] for i in range(바깥쪽 리스트 길이)]
    answer = [[0 for j in range(len(arr1[0]))] for i in range(len(arr1))]
    
    # answer에 arr1과 arr2의 값을 더해준다.
    for i in range(len(arr1)) :
        for j in range(len(arr1[0])) :
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer