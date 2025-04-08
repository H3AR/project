import numpy as np

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 10)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all(tabuleiro[i, :] == jogador) or all(tabuleiro[:, i] == jogador):
            return True
    # Verificar diagonais
    if all(np.diag(tabuleiro) == jogador) or all(np.diag(np.fliplr(tabuleiro)) == jogador):
        return True
    return False

def jogo_da_velha():
    tabuleiro = np.full((3, 3), " ")
    jogador_atual = "X"
    jogadas = 0

    while jogadas < 9:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        
        try:
            linha = int(input("Digite a linha (0, 1 ou 2): "))
            coluna = int(input("Digite a coluna (0, 1 ou 2): "))
        except ValueError:
            print("Entrada inválida! Digite números entre 0 e 2.")
            continue

        if linha not in range(3) or coluna not in range(3):
            print("Posição inválida! Escolha entre 0, 1 ou 2.")
            continue

        if tabuleiro[linha, coluna] != " ":
            print("Posição já ocupada! Escolha outra.")
            continue

        tabuleiro[linha, coluna] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {jogador_atual} venceu!")
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"

    exibir_tabuleiro(tabuleiro)
    print("Empate! O jogo terminou sem vencedores.")

if __name__ == "__main__":
    jogo_da_velha()