from src import DAO as dao, Caixas as cx
from src import estrutura_quantos_filmes, estrutura_analise_filmes, escolha_um_filme, carregar_generos
import os

def main():
    os.system("clear")
    running = True
    while running:
        dao_verificar_filmes = dao()
        num_filmes = dao_verificar_filmes.visualizar("COUNT(*)", "filmes", "", "", one=True)
        tem_filmes = True if num_filmes and num_filmes[0] > 0 else False

        dao_verificar_generos = dao()
        num_generos = dao_verificar_generos.visualizar("COUNT(*)", "generos", "", "", one=True)
        tem_generos = True if num_generos and num_generos[0] > 0 else False

        if not tem_generos:
            carregar_generos()

        cx().inicio()
        if not tem_filmes:
            print("* primeiro escolha a terceira opção para carregar os filmes *")
        print()
        print("1. Análise de filmes (test_1.py)")
        print("2. Recomendação de filmes (test_2.py)")
        print("3. Carregar informações dos filmes no banco")
        print("4. Ver filmes")
        print("5. Sair")
        print()

        try:
            num = input("Escolha uma opção: ")
            os.system("clear")
            num = int(num)
            if num in range(1, 6):

                if num == 1:
                    if tem_filmes:
                        estrutura_analise_filmes()
                    else:
                        cx().sem_filmes()

                elif num == 2:
                    escolha_um_filme()

                elif num == 3:
                    tem_filmes = estrutura_quantos_filmes()

                elif num == 4:
                    if tem_filmes:
                        pass
                    else:
                        cx().sem_filmes()

                else:
                    running = False
            else:
                cx().int_errado()
        except ValueError:
            cx().esperava_int()

if __name__ == "__main__":
    main()