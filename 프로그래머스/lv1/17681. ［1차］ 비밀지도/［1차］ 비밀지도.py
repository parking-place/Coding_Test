def solution(n, arr1, arr2):

    # 맵별로 리스트
    map1 = []                                
    map2 = []
    map_real = []
    
    for i in range(n) :
        map1.append(f'{arr1[i]:016b}'[17-n-1:17])
        map2.append(f'{arr2[i]:016b}'[17-n-1:17])
        map_real.append('')
        
    for i in range(n) :
        str1 = ''
        for j in range(n):
            if ((map1[i][j] == '1') | (map2[i][j] == '1')):
                str1 += '#'
            else :
                str1 += ' '
        map_real[i] = str1
    
    return map_real