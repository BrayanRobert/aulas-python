def produtos(key : str) -> float:
    produtos = {
    "Nescau" : 8.90,
    "Batata" : 4.99,
    "Tomate" : 2.99,
    "Doritos" : 5.00,
    "Nesqik" : 15.50,
    "Fralda" : 7.99,
    "Camisinha" : 3.99,
    "Arroz" : 4.99,
    "Picanha" : 59.70
    }

    return produtos[key]

def comprar(dinheiro : float, produto : str, quantidade : int) -> str:
    if type(produto) != str:
        return "ERROR! PARÂMETRO PRODUTO PRECISA SER STRING"
    elif type(quantidade) != int:
        return "ERROR! PARÂMETRO QUANTIDADE PRECISA SER INTEIRO"
    elif type(dinheiro) != float:
        return "ERRROR! PARÂMETRO DINHEIRO PRECISA SER FLOAT"
    else:
        valor_gasto = produtos(key=produto) * quantidade
        if valor_gasto > dinheiro:
            return "ERROR! VOCÊ NÃO TEM DINHEIRO SUFICIENTE"
        else:
            return f"Você comprou {quantidade} de {produto}"
def sacar(dinheiro : float) -> str:
    valor = float(input("Quanto você quer sacar? "))
    if valor > dinheiro:
        return "ERROR! VOCÊ NÃO TEM DINHEIRO SUFICIENTE"
    else:
        return f"Parabéns! Você sacou R${valor}"
def troco(dinheiro : float, produto : str, quantidade : int) -> str:
    valor_gasto = produtos(key=produto) * quantidade
    troco_recebido = dinheiro - valor_gasto
    if troco_recebido > dinheiro:
        return "ERROR! ERRO DE APLICAÇÃO"
    else:
        return troco_recebido
def cancelar(produto : str, quantidade: int) -> str:
    cancelar_produto = input("Você gostaria de cancelar a compra?  Sim/Não ")
    if cancelar_produto() == "Sim":
        return f"Parabéns você cancelou sua compra de {quantidade} {produto} com sucesso!"
    elif cancelar_produto() == "Não":
        return "Compra foi passada com sucesso"
    else:
        return "Resposta inválida. Apenas responda 'Sim' ou 'Não'"

def sair() -> str:
    return "Mercado fechado!"