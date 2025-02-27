from src import DAO as dao, Caixas as cx, estrutura_carregar_filmes
import os

def main():
    running = True
    while running:
        dao_verificar_filmes = dao()
        num_filmes = dao_verificar_filmes.visualizar("COUNT(*)", "filmes", "", "", one=True)
        tem_filmes = True if num_filmes and num_filmes[0] > 0 else False

        cx().inicio()
        if not tem_filmes:
            print("* primeiro escolha a terceira opção para carregar os filmes *")
        print()
        print("1. Análise de filmes (test_1.py)")
        print("2. Recomendação de filmes (test_2.py)")
        print("3. Carregar informações dos filmes no banco")
        print("4. Sair")
        print()

        try:
            num = int(input("Escolha uma opção: "))
            os.system("clear")
            if num in range(1, 5):

                if num == 1:
                    if tem_filmes:
                        pass
                    else:
                        cx().sem_filmes()

                elif num == 2:
                    if tem_filmes:
                        pass
                    else:
                        cx().sem_filmes()

                elif num == 3:
                    if tem_filmes:
                        cx().filmes_ja_carregados()
                    else:
                        tem_filmes = estrutura_carregar_filmes()

                else:
                    running = False
            else:
                cx().int_errado()
        except ValueError:
            cx().esperava_int()

if __name__ == "__main__":
    main()