from ..utils import Caixas as cx, DAO as dao
import os

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
    running = True
    while running:
        cx().recomendacao_filmes()
        print("1. Sortida")
        print("2. Gênero")
        print("3. Popularidade")
        print("4. Diretor")
        print("5. Elenco")
        print("6. Voltar")
        print()
        try:
            num = int(input("Escolha uma opção de recomendação: "))
            os.system("clear")
            if num in range(1, 7):
                if num == 1:
                    pass
                elif num == 2:
                    pass
                elif num == 3:
                    pass
                elif num == 4:
                    pass
                elif num == 5:
                    pass
                else:
                    running = False
            else:
                cx().int_errado()
        except ValueError:
            cx().esperava_int()