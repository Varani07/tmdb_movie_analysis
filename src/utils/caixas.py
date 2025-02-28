class Caixas():
    @staticmethod
    def int_errado():
        print("---------------------------")
        print("| DIGITE UM NUMERO VÁLIDO |")
        print("---------------------------")
        print()
    @staticmethod
    def esperava_int():
        print("--------------------")
        print("| DIGITE UM NUMERO |")
        print("--------------------")
        print()
    @staticmethod
    def esperava_caracter_valido():
        print("-----------------------------")
        print("| DIGITE UM CARACTER VÁLIDO |")
        print("-----------------------------")
        print()
    @staticmethod
    def sem_filmes():
        print("-------------------------------------")
        print("| PRIMEIRO ESCOLHA A TERCEIRA OPÇÃO |")
        print("-------------------------------------")
        print()
    @staticmethod
    def filmes_ja_carregados():
        print("---------------------------------")
        print("| OS FILMES JÁ FORAM CARREGADOS |")
        print("---------------------------------")
        print()
    @staticmethod
    def filme_nao_encontrado():
        print("-----------------------------------------------")
        print("| NÃO ENCONTRAMOS O FILME QUE ESTÁ PROCURANDO |")
        print("-----------------------------------------------")
        print()
        print(" - primeiro certifique-se de que o filme tenha sido carregado - ")
        print()
    @staticmethod
    def escolha_excede_num_filmes(num_filmes):
        print()
        print(" Escolha excede o número de filmes disponíveis....")
        print(f" Número de filmes disponíveis: {num_filmes}")
        print()
        print()
    @staticmethod
    def filmes_carregados():
        print("----------------------")
        print("| FILMES CARREGADOS! |")
        print("----------------------")
        print()
    @staticmethod
    def inicio():
        print()
        print(" - - -  INÍCIO - - - ")
        print()
        print()
    @staticmethod
    def carregando_filmes():
        print()
        print(" - - -  CARREGANDO FILMES - - - ")
        print()
        print()
    @staticmethod
    def analise_dados_filmes():
        print()
        print(" - - -  Análise de Dados de Filmes - - - ")
        print()
        print()
    @staticmethod
    def recomendacao_filmes():
        print()
        print(" - - -  Recomendação de Filmes - - - ")
        print()
        print()
    @staticmethod
    def info_atores_quantidade_filmes(nome, quantidade, filmes):
        print()
        print(" - - - - - - - - - - - - -")
        print(f" | Nome: {nome}")
        print(f" | Quantidade de filmes que atuou: {quantidade}")
        print(" | Filmes:")
        for filme in filmes:
            print(f" | - {filme}")
    @staticmethod
    def top_atores_bilheteria(num:int, ator:str, info:dict):
        revenue_formatado = f"${info['revenue']:,.2f}"
        print()
        print(" - - - - - - - - - - - - -")
        print(f" {num}. {ator}: {revenue_formatado}")
        print(" | Filmes:")
        for filme, receita in info['filmes'].items():
            receita_formatada = f"${receita:,.2f}"
            print(f" | - {filme}: {receita_formatada}")
    @staticmethod
    def info_quantidade_generos(nome, quantidade):
        print()
        print(" - - - - - - - - - - - - -")
        print(f" | Nome: {nome}")
        print(f" | Quantidade de filmes que contém esse gênero: {quantidade}")
    @staticmethod
    def info_recomendacao(num, nome, id, generos, sinopse):
        print()
        print(" - - - - - - - - - - - - -")
        print(f" {num}. Nome: {nome}    ID: {id}")
        print(f" | Gêneros: {generos}")
        print(f" | Sinopse: {sinopse}")