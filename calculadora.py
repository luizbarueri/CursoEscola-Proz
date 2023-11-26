

sair = 1
while sair != 0:
    print("Digite um numero para A:")
    a = int(input())
    print("Digite um numero:para B")
    b = int(input())
    print("Digite um operador [1, 2, 3, 4]:")
    print("--------------------------------------")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    print("--------------------------------------")
    operador = int(input())
    
    if operador == 1: resultado = a + b
    if operador == 2: resultado = a - b
    if operador == 3: resultado = a * b
    if operador == 4 and b > 0: resultado = a / b
    if operador == 0: sair = 0
    print("Resultado:", resultado)
    
