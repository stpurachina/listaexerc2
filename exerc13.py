class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

#Teste Classe
func1 = Funcionario('Morales Moreno', 1150.90)
print (f'Nome: {func1.getNome()}')
print (f'Salario: R$ {func1.getSalario():.2f}')
