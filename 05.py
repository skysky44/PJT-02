import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()


def search_movie(title):

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': os.getenv('api_key'),
        'language': 'ko-KR',
        'region': 'KR',
        'query': title
    }

    response = requests.get(BASE_URL+path, params=params).json()
    if response['results'] == []:
        return None
    else:
        return response['results'][0]['id']


def recommendation(title):

    movie_id = search_movie(title)  # 다른 함수의 결과값을 이용하기 위해서는 함수를 실생시켜야 한다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/recommendations'
    params = {
        'api_key': '329eece8bd11e0cf9158d9060529cb42',
        'language': 'ko-KR',
        'region': 'KR'
    }
    if movie_id == None:
        return None
    else:
        response = requests.get(BASE_URL+path, params=params).json()
        movie_list = []
        movie_number = len(response['results'])
        for i in range(0, movie_number):
            movie_list.append(response['results'][i]['title'])
        return movie_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
