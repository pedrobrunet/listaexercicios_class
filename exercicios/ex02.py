class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

# --- Fluxo de Entrada do Usuário ---

# 1. Coletamos os dados primeiro
input_titulo = input("Digite o título do livro: ")
input_autor = input("Digite o nome do autor: ")

# 2. Criamos o objeto passando as variáveis que receberam o input
meu_livro = Livro(input_titulo, input_autor)

# 3. Exibimos o resultado
print("\nInformações cadastradas:")
print(meu_livro.detalhes())