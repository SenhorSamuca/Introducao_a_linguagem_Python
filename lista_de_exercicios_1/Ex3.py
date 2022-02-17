print('3 - Escreva um programa que resolva uma equação de segundo grau.')

from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
 
delta = b**2 - 4*a*c
 
if delta < 0:
    print("Delta negativo")
else:
    raiz_delta = sqrt(delta)
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b - raiz_delta)/2*a
 
    print("As raízes são", x1, "e", x2)

print('-' * 100)

"""
Solução alternativa

a = int(input("Digite o valor do coeficiente A: "))
b = int(input("Digite o valor do coeficiente B: "))
c = int(input("Digite o valor do coeficiente C: "))

if a == 0:
    print("Não é equação do segundo grau")

else:
    delta = b**2-4*a*c
    print("O valor de Delta é: ", delta)

    if delta < 0:
        print("Não há soluções reais para a equação")
    elif delta == 0:
        x = -b/2*a
        print("Solução única x = %.3f" %x)
    else:
        x1 = (-b+delta**0.5)/(2*a)
        x2 = (-b-delta**0.5)/(2*a)
        print("O valor de x1 é: ", x1)
        print("O valor de x2 é: ", x2)

print('-' * 100)
"""
