def solution(genres, plays):
    answer = []
    # 장르별로 딕셔너리 생성
    genres_songs = {}
    # 장르별로 재생횟수 딕셔너리 생성
    genres_plays = {}
    
    # 장르별로 인덱스, 총 재생횟수 저장
    for i, genre in enumerate(genres):
        try:
            genres_songs[genre].append(i)
            genres_plays[genre] += plays[i]
        except:
            genres_songs[genre] = [i]
            genres_plays[genre] = plays[i]
    
    # 장르간 총재생횟수 내림차순 정렬
    genres_plays = dict(sorted(genres_plays.items(), key = lambda x: x[1], reverse = True))
    # 장르별 곡들간 재생횟수 내림차순 정렬
    for k in genres_songs.keys():
        genres_songs[k].sort(key = lambda x: plays[x], reverse = True)
        
    print(genres_songs)
    print(genres_plays)
    
    # 장르별로 가장 많이 재생된 두 곡의 인덱스를 answer에 추가
    for k in genres_plays.keys():
        answer.append(genres_songs[k][0])
        try:
            # 장르별 곡이 2개 이상일 경우
            answer.append(genres_songs[k][1])
        except:
            # 장르별 곡이 1개일 경우
            pass
        
    return answer
        