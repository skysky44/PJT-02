import requests
import os
from dotenv import load_dotenv

load_dotenv()


def popular_count():
    api_key = os.getenv('api_key')
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page=1"

    res = requests.get(url=url).json()
    movie_count = len(res['results'])

    return movie_count


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
