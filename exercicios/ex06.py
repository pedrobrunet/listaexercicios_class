class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade # Nomeamos como quantidade para ficar claro

    def calcular_total(self):
        # Apenas retorna o cálculo, sem sobrescrever os atributos
        return self.preco * self.quantidade


meu_produto = Produto("telefone", 1000, 10)

total = meu_produto.calcular_total()
print(f"O valor total do produto {meu_produto.nome} é: R$ {total}")