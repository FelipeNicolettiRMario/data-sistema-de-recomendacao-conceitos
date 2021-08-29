import mariadb
import pandas as pd
from termcolor import colored

from utils.env_variables import *

class DatabaseOperator:

    def __init__(self) -> None:
        
        self.connection = mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=int(port),
            database=database
        )

    def list_table_itens(self) -> None:

        print(colored(pd.read_sql(f'SELECT * FROM {table}',self.connection),'blue'))


    def insert_item_in_table(self,item_name: str, item_recomendation: str):

        cursor = self.connection.cursor() 
        sql = f"INSERT INTO {table}(product_name,recomendation_product) VALUES(?, ?)"

        try:
            cursor.execute(sql,(item_name,item_recomendation))
            self.connection.commit()
            print(colored("ITEM ADICIONADO COM SUCESSO!\n",'blue'))

        except mariadb.Error as e:
            print(colored(f"OCORREU UM ERRO AO ADICIONAR O ITEM: {e}\n"),'red')

    def get_itens_by_name(self, itens_in_cart: list) -> list:
        cursor = self.connection.cursor()
        sql = f"SELECT * FROM {table} WHERE PRODUCT_NAME IN {tuple(itens_in_cart)}"

        try:
            cursor.execute(sql)
            print(colored("ITENS ENCONTRADOS...\n",'blue'))
            return cursor
        
        except mariadb.Error as e:
            print(colored(f"ERRO AO PROCURAR ITENS: {e}\n",'red'))

    def delete_rule(self, rule_id: str) -> None:
        cursor = self.connection.cursor()
        sql = f"DELETE FROM {table} WHERE id={rule_id}"

        try:
            cursor.execute(sql)
            self.connection.commit()
            print(colored(f"REGISTRO {rule_id} EXCLUIDO COM SUCESSO...\n",'blue'))
    
        except mariadb.Error as e:
            print(colored(f"ERRO AO DELETAR O ITEM {rule_id}: {e}\n",'red'))



        



