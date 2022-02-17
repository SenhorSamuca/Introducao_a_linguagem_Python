print('5 - Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.')

n1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador matemático que será usado: ")
n2 = float(input("Digite o segundo número: "))

if (operador == "+"):
    resultado = n1 + n2
elif (operador == "-"):
    resultado = n1 - n2
elif (operador == "*"):
    resultado = n1 * n2
elif (operador == "/"):
    resultado = n1 / n2
else:
    print("Operador inválido!")

print(resultado)

print('-' * 100)
