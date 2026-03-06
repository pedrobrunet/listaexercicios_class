class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}"

# Exemplo de uso:
meu_carro = Carro("Toyota", "Supra", 2025)
print(meu_carro.detalhes())

