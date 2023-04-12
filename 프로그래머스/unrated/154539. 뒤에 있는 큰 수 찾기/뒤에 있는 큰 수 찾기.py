def solution(numbers):
    # 뒷수를 저장할 리스트 생성
    behinds = [0 for _ in range(len(numbers))]
    # 가장 큰 수와 리스트 길이 저장
    max_num = max(numbers)
    len_nums = len(numbers)
    # 현재인덱스 포함 뒤의 배열에서 가장 큰 수를 저장할 리스트 생성
    behind_maxs = [0 for _ in range(len(numbers))]
    
    # 뒤에서부터 순회
    for i in range(-1, -len_nums-1, -1):
        # 가장 큰 수일 경우, 마지막 수일 경우 -1
        if numbers[i] == max_num or i == -1:
            behinds[i] = -1
            behind_maxs[i] = numbers[i]
            continue
        # 현재 수가 뒤의 가장 큰 수보다 크면 -1
        if numbers[i] > behind_maxs[i+1] and behind_maxs[i+1] != 0:
            behinds[i] = -1
            behind_maxs[i] = numbers[i]
            continue
        # 현재 인덱스에서 뒤로 순회하며 큰 수를 찾음
        for j in range(len_nums+i+1, len_nums):
            # 현재 수보다 큰 수를 찾으면 해당 수를 저장
            if numbers[i] < numbers[j]:
                behinds[i] = numbers[j]
                behind_maxs[i] = behind_maxs[j]
                break
            # 현재 수와 같은 수를 찾으면 해당 수의 뒷수를 저장
            if numbers[i] == numbers[j] and behinds[j] != 0:
                behinds[i] = behinds[j]
                behind_maxs[i] = behind_maxs[j]
                break
            # 현재 수보다 큰 뒷수를 찾으면 해당 뒷수를 저장
            if numbers[i] < behinds[j]:
                behinds[i] = behinds[j]
                behind_maxs[i] = behind_maxs[j]
                break
            # 현재 수보다 큰 뒷수를 찾지 못하면 -1 저장
            behinds[i] = -1
                
    return behinds