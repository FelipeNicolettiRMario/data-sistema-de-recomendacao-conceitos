from termcolor import colored
from services.database_operator import DatabaseOperator

class RecomendationService:

    def __init__(self) -> None:
        self.db = DatabaseOperator()

    def analyse_itens(self,itens: list) :

        recomended_items = set()

        items_in_compound_rule = self.db.get_itens_in_compound_rule(itens)
        for items in items_in_compound_rule:
            recomended_items.add(items)

        itens_in_rule = self.db.get_itens_in_rule(itens)

        for recomendation_item in itens_in_rule:
            if recomendation_item not in itens:
                recomended_items.add(recomendation_item)

        print(colored(f"Itens recomendados com base no carrinho: {recomended_items}\n",'blue'))