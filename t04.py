# 파일명이 숫자이면 모듈이 안돼서 이름 변경한 파일
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


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
