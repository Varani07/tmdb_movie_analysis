from utils import Caixas as cx
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
            num = int(input("Escolha uma opção: "))
            os.system("clear")
            if num in range(1, 5):
                if num == 1:
                    pass
                elif num == 2:
                    pass
                elif num == 3:
                    pass
                else:
                    running = False
            else:
                cx().int_errado()
        except ValueError:
            cx().esperava_int()