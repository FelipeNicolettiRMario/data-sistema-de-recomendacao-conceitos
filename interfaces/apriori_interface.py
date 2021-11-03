from apriori import Apriori
from apriori.utils import get_data_from_mariadb
from services.database_operator import DatabaseOperator
from termcolor import colored

class AprioriInterface:

    def __init__(self,transaction_table) -> None:
        
        data = get_data_from_mariadb(transaction_table)
        self.service = Apriori(data)

    def get_result_from_analysis(self):

        return self.service.run_analysis_on_data_set()

    def start(self):

        operator = DatabaseOperator()

        results = self.get_result_from_analysis()

        for result in results:
            
            rule = result.get('rule')

            item_x, item_y = rule.split(' with ')
            operator.insert_rule(item_x,item_y)
            operator.insert_rule(item_y,item_x)

        print(colored("Regras inseridas com sucesso!","green"))