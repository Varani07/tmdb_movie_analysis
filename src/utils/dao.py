from .db import ConexaoBanco
from mysql.connector import Error

class DAO():
    def __init__(self):
        self.connection = ConexaoBanco().get_connection()
        self.cursor = self.connection.cursor()

    def atualizar(self, tabela: str, dados: str, where: str, valor_dados: tuple):
        try:
            sql = f"UPDATE {tabela} SET {dados} WHERE {where}"

            self.cursor.execute(sql, valor_dados)

            self.connection.commit()
            self.cursor.close()
        
        except Error as e:
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected:
                self.connection.close()

    def inserir(self, tabela: str, dados: str, values: str, valor_dados: tuple):
        try:
            sql = f"INSERT INTO {tabela} ({dados}) VALUES ({values})"
            
            self.cursor.execute(sql, valor_dados)

            self.connection.commit()
            self.cursor.close()

        except Error as e:
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected:
                self.connection.close()
        
    def visualizar(self, dados: str, tabela: str, where: str, valor_dados: tuple, one: bool):
        try:
            sql = f"SELECT {dados} FROM {tabela}{where}"

            if valor_dados == "":
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, valor_dados)
            
            if one:
                result = self.cursor.fetchone()
            else:
                result = self.cursor.fetchall()


            self.cursor.close()
            return result
        
        except Error as e:
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected:
                self.connection.close()