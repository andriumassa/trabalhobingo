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

# Função para exibir a cartela
def exibir_cartela(nome, cartela, numeros_sorteados):
    print(f"Cartela do jogador {nome}:")
    for linha in cartela:
        linha_display = []
        for numero in linha:
            if numero in numeros_sorteados:
                linha_display.append(f"[{numero}]")
            else:
                linha_display.append(f" {numero} ")
        print(" | ".join(linha_display))
    print()

# Função para sorteio de números
def sortear_numero(numeros_sorteados, intervalo):
    while True:
        numero = random.randint(intervalo[0], intervalo[1])
        if numero not in numeros_sorteados:
            numeros_sorteados.add(numero)
            return numero

# Função principal para o simulador
def simulador_bingo():
    print("Escolha o modo de jogo:")
    print("1. Modo rápido")
    print("2. Modo demorado")
    modo = int(input("Digite o número correspondente ao modo escolhido: "))
    
    if modo == 1:
        mododejogo = "rápido"
        jogadores = ["Jogador 1", "Jogador 2"]
        num_cartelas = 2
        intervalo_sorteio = (1, 30)
    else:
        mododejogo = "demorado"
        jogadores = ["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4"]
        num_cartelas = 4
        intervalo_sorteio = (1, 40)

    # Gerar cartelas
    cartelas = {jogador: gerar_cartela(mododejogo) for jogador in jogadores}

    # Conjunto para armazenar os números sorteados
    numeros_sorteados = set()

    while True:
        # Sortear um número
        numero_sorteado = sortear_numero(numeros_sorteados, intervalo_sorteio)
        print(f"Número sorteado: {numero_sorteado}")
        print("Dezenas sorteadas até o momento:", sorted(numeros_sorteados))