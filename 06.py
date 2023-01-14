import requests
from pprint import pprint
import t04
import os
from dotenv import load_dotenv

load_dotenv()


def credits(title):

    movie_id = t04.search_movie(title)

    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key': os.getenv('api_key'),
        'language': 'ko-KR',
        'region': 'KR'
    }
    if movie_id == None:
        return None
    else:
        response = requests.get(BASE_URL+path, params=params).json()
        pprint(response)

    result = {
        'cast': [],
        'crew(directing)': []
    }
    for i in range(0, len(response['cast'])):
        if response['cast'][i]['cast_id'] < 10:
            result['cast'].append(response['cast'][i]['name'])

    for i in range(0, len(response['crew'])):
        if response['crew'][i]['department'] == 'Directing':
            result['crew(directing)'].append(response['crew'][i]['name'])

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
