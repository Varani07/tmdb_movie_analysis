import json, os
from ..utils import info_filmes, DAO as dao, Caixas as cx

def carregar_filmes(id_filmes):
        
    for id_filme in id_filmes:
        json_data_info_filmes = info_filmes("info", id_filme)
        data_info_filmes = json.loads(json_data_info_filmes)
        
        try:
            data_info_filmes['success']
            filme_existe = False
        except:
            filme_existe = True

        if not filme_existe:
            print(f"Filme não encontrado: {id_filme}")
        else:
            dao_verificar_filme_db = dao()
            id_existe = dao_verificar_filme_db.visualizar("COUNT(*)", "filmes", " WHERE id_filme = %s", (id_filme,), True)
            
            if id_existe[0] > 0:
                print(f"Filme já foi carregado: {id_filme}")
            else:
                dao_inserir_filme = dao()
                dao_inserir_filme.inserir("filmes", "id_filme, titulo, revenue", "%s, %s, %s", (data_info_filmes["id"], data_info_filmes["title"], data_info_filmes["revenue"]))
                print("Adicionando..." + data_info_filmes["title"])

                for genre_info_filme in data_info_filmes["genres"]:
                    id_genero_info_filme = genre_info_filme["id"]
                    dao_inserir_genero_e_filme = dao()
                    dao_inserir_genero_e_filme.inserir("filme_genero", "id_filme, id_genero", "%s, %s", (id_filme, id_genero_info_filme))

                json_data_cast = info_filmes("elenco", id_filme)
                data_cast = json.loads(json_data_cast)
                for info_elenco in data_cast["cast"]:
                    nome = info_elenco["name"]
                    departamento = info_elenco["known_for_department"]
                    dao_inserir_ator = dao()
                    dao_inserir_ator.inserir("elenco", "id_filme, nome, departamento", "%s, %s, %s", (id_filme, nome, departamento))

def carregar_generos():
    json_data_generos = info_filmes("generos")
    data_generos = json.loads(json_data_generos)

    for genre in data_generos["genres"]:
        id_genero = genre["id"]
        nome_genero = genre["name"]
        dao_inserir_genero = dao()
        dao_inserir_genero.inserir("generos", "id_genero, nome_genero", "%s, %s", (id_genero, nome_genero))

def estrutura_quantos_filmes():
    running = True
    tem_filmes = False
    while running:
        print()
        print(" (Ex. '1439705,1439784,1439883') ")
        try:
            answer = input("Digite a ID dos filmes que gostaria de carregar ou use * para voltar: ")
            os.system("clear")
            answer = answer.strip()
            answer = answer.replace(" ", "")
            answer_teste = answer.replace(",", "")
            int(answer_teste)
            lista_ids = answer.split(",")
            tem_filmes = carregar_filmes(lista_ids)
            
        except ValueError:
            if answer == "*":
                return tem_filmes
            else:
                cx().esperava_caracter_valido()