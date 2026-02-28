class Retangulo:
    def __init__(self,altura, base):
        self.altura = altura
        self.base = base


    def calcular_area(self):
       return self.altura * self.base

input_altura = float(input("Digite o valor da altura: "))
input_base = float(input("Digite o valor da base: "))

meu_retangulo = Retangulo(input_altura, input_base)

area = meu_retangulo.calcular_area()
print(f"A área do retângulo é: {area}")