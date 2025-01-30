import random

# Função para gerar uma cartela de bingo
def gerar_cartela(mododejogo):
    cartela = []
    if mododejogo == "rápido":
        colunas = [
            list(range(1, 11)),  # 1 a 10
            list(range(11, 21)),  # 11 a 20
            list(range(21, 31))   # 21 a 30
        ]
        for c in colunas:
            random.shuffle(c)
        cartela = [
            [colunas[0][0], colunas[1][0], colunas[2][0]],
            [colunas[0][1], colunas[1][1], colunas[2][1]],
        ]
    elif mododejogo == "demorado":
        colunas = [
            list(range(1, 11)),   # 1 a 10
            list(range(11, 21)),  # 11 a 20
            list(range(21, 31)),  # 21 a 30
            list(range(31, 41))   # 31 a 40
        ]
        for c in colunas:
            random.shuffle(c)
        cartela = [
            [colunas[0][0], colunas[1][0], colunas[2][0], colunas[3][0]],
            [colunas[0][1], colunas[1][1], colunas[2][1], colunas[3][1]],
            [colunas[0][2], colunas[1][2], colunas[2][2], colunas[3][2]],
        ]
    return cartela


