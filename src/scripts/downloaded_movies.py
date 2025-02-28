from ..utils import Caixas as cx, DAO as dao
import os

def ver_filmes():
    dao_filmes = dao()
    filmes = dao_filmes.visualizar("id_filme, titulo", "filmes", "", "", False)
    for i, filme in enumerate(filmes, start=1):
        cx().filmes_db(i, filme[1], filme[0])
    print()
    input(" - - - - - - PRESSIONE ENTER PARA VOLTAR - - - - - -")
    os.system("clear")