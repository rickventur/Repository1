import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogo", "desenvolvimento"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

def verificar_palavra_completa(palavra, letras_corretas):
    for letra in palavra:
        if letra not in letras_corretas:
            return False
    return True

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    mostrar_palavra(palavra, letras_corretas)

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente novamente!")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            if verificar_palavra_completa(palavra, letras_corretas):
                print("Parabéns! Você ganhou!")
                break
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letra incorreta! Você tem", tentativas, "tentativas restantes.")

            if tentativas == 0:
                print("Game over! A palavra era:", palavra)
                break

        mostrar_palavra(palavra, letras_corretas)

jogar_forca()
