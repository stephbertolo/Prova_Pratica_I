valorUm = int(input("Escreva o primeiro número. "))
valorDois = int(input("Escreva o segundo número. "))
valorTres = int(input("Escreva o terceiro número. "))

if valorUm > valorDois and valorUm > valorTres:
    print(str(valorUm) + " é o maior número.")

elif valorDois > valorUm and valorDois > valorTres:
    print(str(valorDois) + " é o maior número.")

else:
    print(str(valorTres) + " é o maior número.")