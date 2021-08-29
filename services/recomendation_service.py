from termcolor import colored
from services.database_operator import DatabaseOperator

class RecomendationService:

    def __init__(self) -> None:
        self.db = DatabaseOperator()

    def analyse_itens(self,itens: list) -> str:

        items_in_database = self.db.get_itens_by_name(itens)
        recomended_items = []

        for id_item,name_item,recomendation_item in items_in_database:
            
            if recomendation_item not in itens:
                recomended_items.append(recomendation_item)
        
        print(colored(f"Itens recomendados com base no carrinho: {recomended_items}\n",'blue'))