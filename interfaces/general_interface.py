import sys

from termcolor import colored

from interfaces.database_interface import DatabaseInterface
from interfaces.recomendation_interface import RecomendationInterface
from interfaces.apriori_interface import AprioriInterface

class GeneralInterface:

    def start(self):

        print("BEM VINDO! Escolha uma das opções abaixo para prosseguir...\n")
        option_selected = input(colored("1.Gerenciar Regras\n2.Utilizar sistema de recomendação\n4.Criação de regras com analise apriori\n3.Sair\n\n->",'green'))

        if option_selected == "1":
            DatabaseInterface().start()
            self.start()

        elif option_selected == "2":
            RecomendationInterface().start()
            self.start()

        elif option_selected == "4":
            AprioriInterface('transaction').start()
            self.start()
            
        elif option_selected == "3":
            print(colored("SAINDO DO SISTEMA...",'yellow'))
            sys.exit()


        else:
            print(colored("OPÇÃO INVALIDA...\n",'red'))
            self.start()
    