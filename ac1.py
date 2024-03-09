"""
AC1 
João Lucas Ferraz Meirelles / 202402116495

"""
#Exercício 1
a = int(input("Informe o parâmetro a da equação: "))
b = int(input("Informe o parâmetro b da equação: "))
c = int(input("Informe o parâmetro c da equação: "))

delta = b**2 - 4*a*c
print( "O valor de delta é: ", delta)

x1 = (-b - delta**0.5) / (2*a)
x2 = (-b + delta**0.5) / (2*a)
print(" O valor da primeira raiz é: ", x1)
print(" O valor da segunda raiz é: ", x2)

#Exercício 2
ano = int(input("Informe o ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('False'. format(ano))
else:
    print('True'. format(ano))