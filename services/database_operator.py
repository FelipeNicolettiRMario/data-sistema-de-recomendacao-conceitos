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

    def __insertion(self,query: str, parameters: tuple) -> None:
        cursor = self.connection.cursor() 

        try:
            cursor.execute(query,parameters)
            self.connection.commit()
            print(colored("REGRA ADICIONADA COM SUCESSO!\n",'blue'))

        except mariadb.Error as e:
            print(colored(f"OCORREU UM ERRO AO ADICIONAR A REGRA: {e}\n"),'red')

    def __selection(self, sql: str):

        cursor = self.connection.cursor()

        try:
            cursor.execute(sql)
            print(colored("ITENS ENCONTRADOS...\n",'blue'))
            return cursor
        
        except mariadb.Error as e:
            print(colored(f"ERRO AO PROCURAR ITENS: {e}\n",'red'))

    def __deletion(self, sql: str, parameters: tuple):
        cursor = self.connection.cursor()

        try:
            cursor.execute(sql,parameters)
            self.connection.commit()
            print(colored(f"REGISTRO EXCLUIDO COM SUCESSO...\n",'blue'))
    
        except mariadb.Error as e:
            print(colored(f"ERRO AO DELETAR O ITEM : {e}\n",'red'))

    def list_table_itens(self) -> None:

        print(colored("TABELA DE PRODUTO:\n","yellow"))
        print(colored(pd.read_sql(f'SELECT * FROM product',self.connection),'blue'))
        print('\n\n')

        print(colored("TABELA DE REGRA:\n","yellow"))
        print(colored(pd.read_sql(f'SELECT * FROM rule',self.connection),'blue'))
        print('\n\n')

        print(colored("TABELA DE REGRA COMPOSTA:\n","yellow"))
        print(colored(pd.read_sql(f'SELECT * FROM compound_rule',self.connection),'blue'))
        print('\n\n')

    def get_id_item(self,item_name: str) -> int:
        sql_select = f'SELECT * FROM product WHERE product_name = "{item_name}"'
        result = self.__selection(sql_select)

        if result.arraysize == 1:
            for id,name in result:
                return id 

    def insert_item(self,item_name: str) -> int:
        item_exists = self.get_id_item(item_name)

        if item_exists:
            return item_exists
        
        else:
            sql_insert = f"INSERT INTO product(product_name) value(?)"
            self.__insertion(sql_insert,(item_name))
            return self.get_id_item(item_name)

    def insert_rule(self,item_name: str, item_recomendation: str):

        id_item_name = self.insert_item(item_name)
        item_recomendation_id = self.insert_item(item_recomendation)

        sql = f"INSERT INTO rule(product_base,product_recomendation) VALUES(?, ?)"

        self.__insertion(sql,(id_item_name,item_recomendation_id))

    def insert_compound_rule(self,item_a: str, item_b: str, item_recomendation: str):

        id_item_a = self.insert_item(item_a)
        id_item_b = self.insert_item(item_b)
        id_item_recomendation = self.insert_item(item_recomendation)

        sql = "INSERT INTO compound_rule(product_a,product_b,product_recomendation) VALUES(?, ?, ?)"

        self.__insertion(sql,(id_item_a,id_item_b,id_item_recomendation))

    def get_itens_in_compound_rule(self, itens_in_cart: list) -> list:

        id_itens_in_cart = str([self.get_id_item(item) for item in itens_in_cart]).replace('[','(').replace(']',')')
        sql = f"SELECT * FROM compound_rule WHERE product_a IN {id_itens_in_cart} or product_b IN {id_itens_in_cart}"

        self.__selection(sql)
    def get_itens_in_rule(self, itens_in_cart: list) -> list:

        id_itens_in_cart = str([self.get_id_item(item) for item in itens_in_cart]).replace('[','(').replace(']',')')
        sql = f"SELECT * FROM rule WHERE product_base IN {id_itens_in_cart}"

        self.__selection(sql)

    def delete_rule(self, product_name: str) -> None:
        product_id = self.get_id_item(product_name)

        sql = "DELETE FROM rule WHERE product_base= (?)"

        self.__deletion(sql,(product_id,''))

    def delete_compound_rule(self, product_a: str, product_b) -> None:

        id_item_a = self.insert_item(product_a)
        id_item_b = self.insert_item(product_b)

        sql = f"DELETE FROM compound_rule WHERE product_a= (?) AND product_b= (?)"
        
        self.__deletion(sql,(id_item_a,id_item_b))


        



