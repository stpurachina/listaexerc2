class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento / 100.0)
        
#Teste Classe
harry = Funcionario("Harry", 25000)
harry.aumentarSalario(10)
print (f'Nome: {harry.getNome()}')
print (f'Salario: R$ {harry.getSalario():.2f}')
