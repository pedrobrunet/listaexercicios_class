import math

class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def calcula_area(self):
        area = math.pi * self.raio ** 2
        return area


meu_circulo = Circulo(5)
area = meu_circulo.calcula_area()
print(f"A área do círculo com raio {meu_circulo.raio} é: {area:.2f}")