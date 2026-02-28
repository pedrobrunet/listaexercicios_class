class Contabancaria:
    def __init__(self, Saldo, Titular):
        self.saldo = 0
        self.titular = Titular

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("O valor do saque deve ser positivo.")


# 1. Criando uma conta para o titular João Pedro
minha_conta = Contabancaria(0, "João Pedro Brunet")

# 2. Testando o depósito
print(f"Titular: {minha_conta.titular}")
minha_conta.depositar(150.00) # Saldo deve ir para 150
minha_conta.depositar(50.00)  # Saldo deve ir para 200

# 3. Testando o saque
minha_conta.sacar(70.00)      # Saldo deve ir para 130
minha_conta.sacar(300.00)     # Deve exibir "Saldo insuficiente!"

# 4. Verificando o saldo final
print(f"Saldo atual de {minha_conta.titular}: R${minha_conta.saldo}")



