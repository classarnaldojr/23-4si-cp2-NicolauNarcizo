import cv2

# Função para identificar a jogada com base na posição da mão no vídeo
def identificar_jogada(x, y, largura, altura, largura_video):
    margem = largura_video // 3
    if x < margem:
        return "Jogador 1: Pedra"
    elif x > largura_video - margem:
        return "Jogador 2: Tesoura"
    else:
        if y < altura // 2:
            return "Jogador 1: Papel"
        else:
            return "Jogador 2: Papel"

# Função para comparar as jogadas e determinar o vencedor
def determinar_vencedor(jogada1, jogada2):
    if jogada1 == jogada2:
        return "Empate"
    elif jogada1 == "Pedra" and jogada2 == "Tesoura":
        return "Jogador 1 venceu"
    elif jogada1 == "Papel" and jogada2 == "Pedra":
        return "Jogador 1 venceu"
    elif jogada1 == "Tesoura" and jogada2 == "Papel":
        return "Jogador 1 venceu"
    else:
        return "Jogador 2 venceu"

# Carregar o vídeo
video = cv2.VideoCapture('pedra-papel-tesoura.mp4')

# Loop para processar cada quadro do vídeo
while True:
    ret, frame = video.read()
    if not ret:
        break

    altura, largura, _ = frame.shape

    # Identificar a posição da mão dos jogadores
    jogada1 = identificar_jogada(0, altura // 2, largura, altura, largura)
    jogada2 = identificar_jogada(largura - 1, altura // 2, largura, altura, largura)

    # Determinar o vencedor
    resultado = determinar_vencedor(jogada1.split(": ")[1], jogada2.split(": ")[1])

    # Exibir o resultado no frame
    cv2.putText(frame, jogada1, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, jogada2, (20, altura - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, resultado, (20, altura // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Exibir o frame
    cv2.imshow('Jogo de Pedra, Papel e Tesoura', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
video.release()
cv2.destroyAllWindows()
