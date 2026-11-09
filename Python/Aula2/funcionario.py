class Funcionario():
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        print(f"Salário: R${self.salario_base}")

class Gerente(Funcionario):
    def bonus(self):
        bonus = int(input("Qual o bonus?"))
        self.salario_base += bonus

class Vendedor(Funcionario):
    def comissao(self):
        comissao = int(input("Qual a comissao?"))
        vendas = int(input("Quantas vendas?"))
        self.salario_base += (comissao * vendas)

pedro = Funcionario("pedro", "1000")
marcos = Gerente("marcos", 5000)
andre = Vendedor("andre", 3000)

marcos.calcular_salario()
marcos.bonus()
marcos.calcular_salario()

andre.calcular_salario()
andre.comissao()
andre.calcular_salario()