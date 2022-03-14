from collections import defaultdict

def solution(genres, plays):
    answer = []
    play_dict = {}
    # 초기화 편하게 하기 위한 defaultdict 활용
    song_dict = defaultdict(dict)
    
    # 각 장르별 총 재생 수와 정렬을 위한 nested dict 구성
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in play_dict:
            play_dict[g] = p
        else:
            play_dict[g] += p
        song_dict[g][i] = p
    
    # 가장 많이 재생된 장르 부터
    for genre in [x[0] for x in sorted(play_dict.items(), key = lambda x : x[1], reverse=True)]:
        cnt = 0
        # 가장 플레이 수가 많은 노래들 중 고유 번호 낮은 순
        # items로 꺼내면 key 오름차순 정렬되서 나옴
        for i, p in sorted(song_dict[genre].items(), key = lambda x : x[1], reverse=True):
            answer.append(i)
            cnt += 1
            if cnt == 2:
                break
        cnt = 0
        
    return answer