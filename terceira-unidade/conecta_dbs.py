from psycopg2 import *
from dotenv import load_dotenv
import os

load_dotenv()


class ConectaPostgre:

    """ Classe com funções de conexão com o Postgre database """

    def __init__(self):
        self.conecta = None

    def connect_bd(self):
        try:
            pwd = os.getenv("DB_PASSWORD")
            host = os.getenv("HOST")

            self.conecta = connect(
                host=host,
                password=pwd,
                database="Trab_final",
                port="5432",
                user="postgres"
                )
        
        except Error as e:
            print(f"Erro ao reconhecer o banco de dados {e}")
            return None
        else:
            print("Database conectado com sucesso!")
            return self.conecta

    def encerra_connect(self):
        if self.conecta:
            self.conecta.close()

class ConectaMongo:
    """ Classe com funções para realizar e gerenciar conexão com o database MongoDB """

    pass