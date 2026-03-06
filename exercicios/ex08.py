class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

# --- Entrada de Dados ---
nome_input = input("Digite o nome do aluno: ")
lista_notas = []

# Loop para receber 3 notas
for i in range(1, 4):
    nota = float(input(f"Digite a nota {i}: "))
    lista_notas.append(nota)

# Criando o objeto
aluno_joao = Aluno(nome_input, lista_notas)

# --- Imprimindo a Média ---
# Usamos f-string para facilitar a leitura e :.2f para arredondar
print("-" * 30)
print(f"O aluno {aluno_joao.nome} obteve a média: {aluno_joao.calcular_media():.2f}")