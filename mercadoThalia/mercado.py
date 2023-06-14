def produtos(key: str) -> float:
    # Dicionário contendo os produtos e seus preços
    produtos = {
        "Nescau": 9.90,
        "Batata": 3.99,
        "Tomate": 5.99,
        "pimenta": 2.00,
        "chocolate": 10.00,
        "ervilha": 7.99,
        "frango": 15.99,
        "Arroz": 12.99,
        "Picanha": 79.70
    }

    return produtos[key]  # Retorna o valor correspondente à chave 'key' no dicionário 'produtos'


def comprar(dinheiro: float, produto: str, quantidade: int) -> str:
    if type(produto) != str:  # Verifica se o tipo do parâmetro 'produto' não é uma string
        return "ERROR! PARÂMETRO (PRODUTO) PRECISA SER STRING"
    elif type(quantidade) != int:  # Verifica se o tipo do parâmetro 'quantidade' não é um inteiro
        return "ERROR! PARÂMETRO (QUANTIDADE) PRECISA SER INTEIRO"
    elif type(dinheiro) != float:  # Verifica se o tipo do parâmetro 'dinheiro' não é um float
        return "ERROR! PARÂMETRO (DINHEIRO) PRECISA SER FLOAT"
    else:
        valor_gasto = produtos(key=produto) * quantidade  # Calcula o valor gasto multiplicando o preço do produto pela quantidade
        if valor_gasto > dinheiro:  # Verifica se o valor gasto é maior que o dinheiro disponível
            return "ERROR! VOCÊ NÃO TEM DINHEIRO SUFICIENTE SEU POBRE"
        else:
            return f"Você comprou {quantidade} de {produto}"  # Retorna uma mensagem informando a compra

def sacar_dinheiro(valor):
    notas_disponiveis = [100, 50, 20, 10, 5, 2, 1]
    quantidade_notas = [0, 0, 0, 0, 0, 0, 0]
    
    for i in range(len(notas_disponiveis)):
        while valor >= notas_disponiveis[i]:
            valor -= notas_disponiveis[i]
            quantidade_notas[i] += 1
    
    if valor != 0:
        print("Não é possível sacar esse valor com as notas disponíveis.")
    else:
        print("Você recebeu as seguintes notas:")
        for i in range(len(notas_disponiveis)):
            if quantidade_notas[i] > 0:
                print(f"{quantidade_notas[i]} nota(s) de R${notas_disponiveis[i]}")

def sair() -> str:
    return "Mercado fechado!"  # Retorna uma mensagem indicando que o mercado está fechado


