class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self,mensagem):
        print(f"{self.nome} diz: {mensagem}")

# --- Testando a classe ---
p1 = Pessoa("João Pedro", 20)
p1.falar("Estou aprendendo POO em Python!")

p2 = Pessoa("Larissa", 20 )
p2.falar("Muito bem !!")