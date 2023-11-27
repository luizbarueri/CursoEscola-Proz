usuario = False

while usuario == False:
    print("Nome completo:")
    nome = input()
    print("Ano de nascimento:")
    anoNasc = int(input())

    if anoNasc >= 1922 and anoNasc <=2021:
        idade = 2053 - anoNasc
        usuario = True
        print("Usuário %s terá %s anos em 2053" %(nome, str(idade)))
    else: 
        print("Ano de nascimento Incorreto, digite maior ou igual a 1922!")