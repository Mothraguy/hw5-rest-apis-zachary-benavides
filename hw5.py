import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_top_10_weekly_trending_movies():
    TMDB_MOVIE_SEARCH_API_REQUEST = f'https://api.themoviedb.org/3/trending/all/day'

    response = requests.get(
        TMDB_MOVIE_SEARCH_API_REQUEST,
        params={
          'api-key': os.getenv('TMDB_API_KEY')
      }
    )

    json_data = response.json()
    pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)
    print(pretty_json_data)

    weekly_trending_movie_object = json_data
    weekly_trending_move_list = weekly_trending_movie_object['results'][0]['title']

    for i in range(10):
       print(weekly_trending_move_list)
