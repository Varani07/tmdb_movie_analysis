import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TMDB_API_KEY")

def info_filmes(tipo, id_filme=0):
    if tipo == "filmes":
        url_especifica = "movie/changes?page=1"
    elif tipo == "atores":
        url_especifica = f"movie/{id_filme}/credits?language=en-US"
    elif tipo == "info":
        url_especifica = f"movie/{id_filme}?language=en-US"
    elif tipo == "recomendacao":
        url_especifica = f"movie/{id_filme}/recommendations?language=en-US&page=1"
    else:
        url_especifica = "genre/movie/list?language=en"

    url = f"https://api.themoviedb.org/3/{url_especifica}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)

    return response.text