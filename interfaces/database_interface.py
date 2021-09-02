from services.database_operator import DatabaseOperator
from termcolor import colored

class DatabaseInterface:

    def __init__(self) -> None:
        self.db = DatabaseOperator()

    def visualize_rules(self) -> None:
        self.db.list_table_itens()

    def get_rule_type(self) -> None:

        rule_type = input("Digite qual o tipo de regra você irá utilizar\n\n1.Regra Simples\n2.Regra Composta\n\n->")

        if rule_type == '1':
            return 'simple'
        
        return 'compound'

    def add_rule(self) -> None:

        item_name = input(colored("Digite o nome do produto: ","green"))
        recomendation_item = input(colored("\nDigite o nome do produto que ele deve recomendar: ",'green'))

        self.db.insert_rule(item_name,recomendation_item)

    def add_compound_rule(self) -> None:
        item_a_name = input(colored("Digite o nome do produto A: ","green"))
        item_b_name = input(colored("Digite o nome do produto B: ","green"))
        recomendation_product = input(colored("Digite o produto a ser recomendado: ","green"))

        self.db.insert_compound_rule(item_a_name,item_b_name,recomendation_product)

    def set_rule_type_insertion(self) -> None:

        rule_type = self.get_rule_type()

        if rule_type == 'simple':
            self.add_rule()
        
        else:
            self.add_compound_rule()

    def delete_rule(self) -> None:

        rule_product = input("Digite o nome do produto para excluir a regra: ")
        self.db.delete_rule(rule_product)

    def delete_compound_rule(self) -> None:
        rule_product_a = input("Digite o nome do produto A para excluir a regra: ")
        rule_product_b = input("Digite o nome do produto B para excluir a regra: ")

        self.db.delete_compound_rule(rule_product_a,rule_product_b)

    def set_rule_type_delete(self) -> None:
        rule_type = self.get_rule_type()

        if rule_type == 'simple':
            self.delete_rule()
        
        else:
            self.delete_compound_rule()

    def start(self) -> None:

        print("Selecione a operacão que você quer realizar:\n")
        option_selected = input(colored("1.Visualizar regras\n2.Adicionar Regra\n3.Excluir regra\n4.Sair\n\n->",'green'))
        

        if option_selected != "4":
            
            process = {
                "1":self.visualize_rules,
                "2":self.set_rule_type_insertion,
                "3":self.set_rule_type_delete
            }

            try:
                process[option_selected]()
                print(colored("Operação realizada com sucesso, voltando ao menu...\n\n",'yellow'))
            except Exception as e:
                print(e)
                print(colored("Operação invalida, voltando ao menu...\n\n",'red'))
            self.start()


        
