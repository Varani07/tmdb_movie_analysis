from mysql.connector import Error, connect
import time

class ConexaoBanco():
    def get_connection(self):
        connection = None
        for tentativa in range(10):
            try:
                connection = connect(
                    host="db",
                    user="root",
                    password="root",
                    database="tmdb_movie_analysis")
                return connection
            except Error as e:
                print(f"Tentativa {tentativa + 1}/10: Banco de dados não está pronto. Erro: {e}")
                time.sleep(5)
        print("Falha ao conectar ao banco de dados após 10 tentativas.")
        return None