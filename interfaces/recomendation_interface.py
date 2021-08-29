from termcolor import colored
from services.recomendation_service import RecomendationService

class RecomendationInterface:

    def __init__(self) -> None:
        self.recomendation_service = RecomendationService()

    def input_itens(self):
        cart_itens = input("Digite is itens no carrinho: ").split(',')
        self.recomendation_service.analyse_itens(cart_itens)

    def start(self):

        print("Selecione a operacão que você quer realizar:\n")
        option_selected = input(colored("1.Verificar recomendação por carrinho\n2.Sair\n\n->",'green'))

        if option_selected != "2":
            
            process = {
                "1":self.input_itens,
            }

            try:
                process[option_selected]()
                print(colored("Operação realizada com sucesso, voltando ao menu...\n\n",'yellow'))
            except:
                print(colored("Operação invalida, voltando ao menu...\n\n",'red'))
            self.start()
