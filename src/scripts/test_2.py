from ..utils import Caixas as cx, DAO as dao, info_filmes
import os, json

def escolha_um_filme():
    running = True
    while running:
        cx().recomendacao_filmes()
        try:
            answer = input("Digite o ID de um filme ou * para voltar: ")
            os.system("clear")
            int(answer)

            dao_pesquisar_id_filme = dao()
            id_filme_existe = dao_pesquisar_id_filme.visualizar("COUNT(*)", "filmes", " WHERE id_filme = %s", (answer,), True)
            if id_filme_existe[0] > 0:
                recomendacao_filmes(answer)
            else:
                cx().filme_nao_encontrado()

        except ValueError:
            if answer == "*":
                running = False
            else:
                cx().esperava_caracter_valido()

def recomendacao_filmes(id_filme):
    json_data_recomendacoes = info_filmes("recomendacao", id_filme)
    data_info_recomendacoes = json.loads(json_data_recomendacoes)
    for i, info_recomendacoes in enumerate(data_info_recomendacoes["results"], start=1):
        generos = []
        for id_genre in info_recomendacoes["genre_ids"]:
            dao_nome_genero = dao()
            nome_genero = dao_nome_genero.visualizar("nome_genero", "generos", " WHERE id_genero = %s", (id_genre,), True)
            generos.append(nome_genero[0])
        str_generos = ', '.join(generos)
        cx().info_recomendacao(i, info_recomendacoes["title"], info_recomendacoes["id"], str_generos, info_recomendacoes["overview"])
        if i == 5:
            break
    print()
    input(" - - - - - - PRESSIONE ENTER PARA VOLTAR - - - - - -")
    os.system("clear")