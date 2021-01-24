# Q. 멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.

# 노래는 인덱스 구분하며, 노래를 수록하는 기준은 다음과 같다.

# 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.

# 노래의 장르를 나타내는 문자열 배열 genres
# 노래별 재생 횟수를 나타내는 정수 배열 plays 주어질 때,

# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.


# 해시 이용

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# 3. 장르 내에서 재생 횟수가 같다면 고유번호가 낮은 노래 먼저 수록

# 장르별(key)로 재생된 횟수(value) 저장
# 장르별 곡의 정보 (index , 재생횟수) 배열로 묶어 저장

# 다시한번 살펴보기

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, _value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre]
        sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0])
    return result


print(get_melon_best_album(genres, plays))
