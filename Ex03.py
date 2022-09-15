letraCorreta = "T"
chances = 0

print("Bem vindo ao Jogo da Forca!")

while chances < 5:

    letraAdivinhada = input("Digite uma letra em maiúsculo: ")

    if letraAdivinhada == letraCorreta:
        print("Parabéns! Você acertou!")
        break

    else:
        print("Infelizmente você errou! Tente novamente.")
        chances += 1