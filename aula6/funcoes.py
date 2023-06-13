def mercadorias(key : str) -> float: #Os nomes são considerados strings e os valores float
    mercadorias = {
        "Nescau": 8.00,
        "Batata" : 5.00,
        "Cenoura" : 3.75,
        "Doritos" : 7.50,
        "Ruffles" : 5.89,
        "Arroz" : 6.00,
        "Feijão" : 8.50,
        "Carne" : 49.89
    }

    return mercadorias[key] #Retorna os produtos para as operações seguintes

def comprar(dinheiro: float, mercadoria: str, quantidade: int) -> str:
    if type(mercadoria) != str:
        return "ERROR! Parametro: Produto precisa ser STRING"
    elif type(quantidade) != int:
        return "ERROR! Parametro: Quantidade precisa ser INTEIRO"
    elif type(dinheiro) != float:
        return "ERROR! Parametro: Dinheiro precisa ser FLOAT"
    else:
        valor_gasto = mercadorias(key = mercadoria)*quantidade #Chama a função mercadorias e utiliza a variavel criada na linha 15 mercadoria
        if valor_gasto > dinheiro:
            return "ERROR! Tu é POBRE menor!!!"
        else:
            return f"Tu comprou {quantidade} de {mercadoria} tá fudido da grana, hein\n Sobrou: {dinheiro - valor_gasto}"
    

def sacar(dinheiro: float) -> str:
    valor = float(input("Tu saca com meu saco? Quer quanto?"))
    if valor > dinheiro:
        return "ERROR! HAHAHA POBRE IMUNDO"
    else:
        return f"RECEBA!!!: {valor}"

def sair() -> str:
    return "Bora mlk mete o pé"