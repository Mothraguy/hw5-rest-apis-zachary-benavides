import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_top_10_weekly_trending_movies():
    # TMDB_MOVIE_PATH = '/p/exports/movie_ids_MM_DD_YYYY.json.gz'
    TMDB_MOVIE_SEARCH_API_REQUEST = f'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1'

    response = requests.get(
        TMDB_MOVIE_SEARCH_API_REQUEST,
        params={
          'api_key': os.getenv('TMDB_API_KEY'),
      }
    )

    json_data = response.json()
    pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)
    print(pretty_json_data)

    weekly_trending_movie_object = json_data
    weekly_trending_movie_list = weekly_trending_movie_object['results'][0]['title']

    article_objects = json_data['response']['docs']

    for i in range(10):
        print(weekly_trending_movie_list['results'][i]['title'])
