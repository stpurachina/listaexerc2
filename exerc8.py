class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida): 
        self.bucho.append(comida)

    def verBucho(self):
        print(f'O bucho do Macaco {self.nome} possui dentro dele:\n {self.bucho}')

    def digerir(self):
        comida_permitida = ['banana','pera','manga']
        for i in range(len(self.bucho)):
            if self.bucho[i] in comida_permitida:
                print(f'O item {self.bucho[i]} foi digerido no bucho do Macaco {self.nome}')
            else:
                print(f'O item {self.bucho[i]} não foi digerido no bucho do Macaco {self.nome}, ele o vomitou')

#Teste Classe
Macaco1 = Macaco('Xita') 
Macaco2 = Macaco('Mamaco') 

Macaco1.comer('abacaxi')
Macaco1.comer('limão')
Macaco1.comer('pera')
Macaco1.verBucho()
Macaco1.digerir()
print('\n')
Macaco2.comer('banana')
Macaco2.comer('laranja')
Macaco2.comer('manga')
Macaco2.comer(Macaco1)
Macaco2.verBucho()
Macaco2.digerir()
