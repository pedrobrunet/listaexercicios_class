class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        # Cálculo: salário atual + (salário atual * percentual / 100)
        self.salario += (self.salario * percentual / 100)

# Entrada de teclado
nome_f = input("\nNome do funcionário: ")
salario_f = float(input("Salário atual: R$ "))
cargo_f = input("Cargo: ")

func = Funcionario(nome_f, salario_f, cargo_f)

# Aplicando o aumento
perc = float(input(f"Qual o percentual de aumento para {func.nome}? "))
func.aumentar_salario(perc)

print(f"Novo salário de {func.nome} ({func.cargo}): R$ {func.salario:.2f}")