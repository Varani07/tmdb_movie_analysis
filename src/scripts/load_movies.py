import json, os
from utils import info_filmes, DAO as dao, Caixas as cx

def carregar_filmes():
    json_data_generos = info_filmes("generos")
    data_generos = json.loads(json_data_generos)

    for genre in data_generos["genres"]:
        id_genero = genre["id"]
        nome_genero = genre["name"]
        dao_inserir_genero = dao()
        dao_inserir_genero.inserir("generos", "id_genero, nome_genero", "%s, %s", (id_genero, nome_genero))

    json_data_id_filmes = info_filmes("filmes")
    data_id_filmes = json.loads(json_data_id_filmes)
    id_filmes = [filme["id"] for filme in data_id_filmes["results"]]

    for id_filme in id_filmes:
        json_data_info_filmes = info_filmes("info", id_filme)
        data_info_filmes = json.loads(json_data_info_filmes)
        dao_inserir_filme = dao()
        dao_inserir_filme.inserir("filmes", "id_filme, titulo, revenue", "%s, %s, %s", (data_info_filmes["id"], data_info_filmes["title"], data_info_filmes["revenue"]))

        for genre_info_filme in data_info_filmes["genres"]:
            id_genero_info_filme = genre_info_filme["id"]
            dao_inserir_genero_e_filme = dao()
            dao_inserir_genero_e_filme.inserir("filme_genero", "id_filme, id_genero", "%s, %s", (id_filme, id_genero_info_filme))

        json_data_ator = info_filmes("atores", id_filme)
        data_ator = json.loads(json_data_ator)
        nome_atores = [ator["name"] for ator in data_ator["cast"]]
        for nome_ator in nome_atores:
            dao_inserir_ator = dao()
            dao_inserir_ator.inserir("atores", "id_filme, nome_ator", "%s, %s", (id_filme, nome_ator))

    cx().filmes_carregados()    

def estrutura_carregar_filmes():
    running = True
    while running:
        cx().carregando_filmes()
        print("1 - Carregar todos os Filmes da primeira página.")
        print("2 - Carregar quantidade personalizada.")
        print("3 - Voltar")
        print()
        try:
            num = int(input("Escolha uma opção: "))
            os.system("clear")
        except ValueError:
            cx().esperava_int()
