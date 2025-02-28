import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("TMDB_API_KEY")

def info_filmes(tipo, id_filme=0):
    if tipo == "elenco":
        url_especifica = f"movie/{id_filme}/credits"
    elif tipo == "info":
        url_especifica = f"movie/{id_filme}"
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

# teste = info_filmes("elenco", 12)
# teste = json.loads(teste)

# for info in teste["cast"]:
#     print(info["known_for_department"], info["name"])

# print(teste["id"],teste["title"],teste["revenue"])

# print(teste["success"])