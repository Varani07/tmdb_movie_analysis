from ..utils import Caixas as cx, DAO as dao
import os

def estrutura_analise_filmes():
    running = True
    while running:
        cx().analise_dados_filmes()
        print("1. Participação por ator.")
        print("2. Frequência de gêneros.")
        print("3. Top 5 Atores com maior bilheteria.")
        print("4. Voltar.")
        print()
        try:
            
            num = input("Escolha uma opção: ")
            os.system("clear")
            int(num)
            if num in range(1, 5):
                if num == 1:
                    participacao_atores()
                elif num == 2:
                    quantidade_generos()
                elif num == 3:
                    bilheteria_atores()
                else:
                    running = False
            else:
                cx().int_errado()
        except ValueError:
            cx().esperava_int()

def participacao_atores():
    nomes = lista_de_atores()
    contagem = {}
    for ator in nomes:
        contagem[ator] = contagem.get(ator, 0) + 1

    resultado = set(contagem.items())
    resultado = sorted(list(resultado), key=lambda x: x[1], reverse=True)
    resultado = [r for r in resultado[:10]]

    for ator_info in resultado:
        dao_pegar_id_filme = dao()
        
        id_filmes = dao_pegar_id_filme.visualizar("id_filme", "elenco", " WHERE nome = %s AND departamento = 'Acting'", (ator_info[0],), False)
        nome_filmes = []
        for id_filme in id_filmes:
            dao_pegar_nome_filme = dao()
            nome_filme = dao_pegar_nome_filme.visualizar("titulo", "filmes", " WHERE id_filme = %s", (id_filme[0],), True)
            nome_filmes.append(nome_filme[0])
        cx().info_atores_quantidade_filmes(ator_info[0], ator_info[1], nome_filmes)
    print()
    input(" - - - - - - PRESSIONE ENTER PARA VOLTAR - - - - - -")
    os.system("clear")

def quantidade_generos():
    dao_ids_generos = dao()
    ids_generos = dao_ids_generos.visualizar("id_genero", "filme_genero", "", "", False)
    generos = []
    for id_genero in ids_generos:
        dao_nome_genero = dao()
        nome_genero = dao_nome_genero.visualizar("nome_genero", "generos", " WHERE id_genero = %s", (id_genero[0],), True)
        generos.append(nome_genero[0])
    contagem = {}

    for genero in generos:
        contagem[genero] = contagem.get(genero, 0) + 1

    resultado = set(contagem.items())
    resultado = sorted(list(resultado), key=lambda x: x[1], reverse=True)
    resultado = [r for r in resultado[:10]]

    for genero_info in resultado:
        cx().info_quantidade_generos(genero_info[0], genero_info[1])
    print()
    input(" - - - - - - PRESSIONE ENTER PARA VOLTAR - - - - - -")
    os.system("clear")

def bilheteria_atores():
    nomes = lista_de_atores()
    nomes = list(set(nomes))

    atores = {}
    for nome in nomes:
        filmes = {}
        bilheteria = 0
        info_final = {}
        dao_pegar_id_filme = dao()
        id_filmes = dao_pegar_id_filme.visualizar("id_filme", "elenco", " WHERE nome = %s", (nome,), False)

        for id_filme in id_filmes:
            dao_pegar_nome_filme = dao()
            info_filme = dao_pegar_nome_filme.visualizar("titulo, revenue", "filmes", " WHERE id_filme = %s", (id_filme[0],), True)
            filmes[info_filme[0]] = info_filme[1]
            bilheteria += info_filme[1]
        info_final['revenue'] = bilheteria
        info_final['filmes'] = filmes
        atores[nome] = info_final

    atores_ordenados = dict(sorted(atores.items(), key=lambda x: x[1]['revenue'], reverse=True)[:5])
    
    for i, (ator, info) in enumerate(atores_ordenados.items(), start=1):
        cx().top_atores_bilheteria(i, ator, info)
    print()
    input(" - - - - - - PRESSIONE ENTER PARA VOLTAR - - - - - -")
    os.system("clear")

def lista_de_atores():
    dao_nome_atores = dao()
    nome_atores = dao_nome_atores.visualizar("nome", "elenco", " WHERE departamento = 'Acting'", "", False)
    nomes = []
    for nome in nome_atores:
        nomes.append(nome[0])
    return nomes