from services.database_operator import DatabaseOperator
from termcolor import colored

class DatabaseInterface:

    def __init__(self) -> None:
        self.db = DatabaseOperator()

    def visualize_rules(self) -> None:
        self.db.list_table_itens()

    def add_rule(self) -> None:

        item_name = input("Digite o nome do produto: ")
        recomendation_item = input(colored("\nDigite o nome do produto que ele deve recomendar: ",'green'))

        self.db.insert_item_in_table(item_name,recomendation_item)

    def delete_item(self) -> None:

        id_rule = input("Digite o id da regra: ")
        self.db.delete_rule(id_rule)

    def start(self) -> None:

        print("Selecione a operacão que você quer realizar:\n")
        option_selected = input(colored("1.Visualizar regras\n2.Adicionar Regra\n3.Excluir regra\n4.Sair\n\n->",'green'))
        

        if option_selected != "4":
            
            process = {
                "1":self.visualize_rules,
                "2":self.add_rule,
                "3":self.delete_item
            }

            try:
                process[option_selected]()
                print(colored("Operação realizada com sucesso, voltando ao menu...\n\n",'yellow'))
            except:
                print(colored("Operação invalida, voltando ao menu...\n\n",'red'))
            self.start()


        
