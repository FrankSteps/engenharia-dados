from psycopg2 import *
from dotenv import load_dotenv
import os

load_dotenv()

class CRUDlogic:

    def __init__():
        pass

    def connect_bd(self):
        try:
            pwd = os.getenv("DB_PASSWORD")

            self.conecta = connect(
                host="localhost",
                password=pwd,
                database="Trab_final",
                port="5432",
                user="postgres"
                )
        except:
            print("Erro ao reconhecer banco de dados")
        else:
            print("Database reconhecido com sucesso")
