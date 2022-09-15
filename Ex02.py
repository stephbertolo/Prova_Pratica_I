idadeTrabalhador = int(input("Digita sua idade: "))
anosTrabalhados = int(input("Digite quantos anos você trabalhou: "))

idadeParaAposentar = 65
anosParaAposentar = 30

idadeParaAposentarII = 60
anosParaAposentarII = 25

if idadeTrabalhador == idadeParaAposentar:
    print("Você pode se aposentar!")

elif anosTrabalhados == anosParaAposentar:
    print("Você pode se aposentar!")

elif idadeTrabalhador == idadeParaAposentarII and anosTrabalhados == anosParaAposentarII:
    print("Você pode se aposentar!")

else:
    print("VocÊ NÃO pode aposentar!")