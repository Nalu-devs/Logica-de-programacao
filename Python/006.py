# Peça para o usuário informar seu nome, seu ano de nascimento e o ano atual. Exiba sua idade

nome = input()
anoNasc = int(input())
anoAtual = int(input())
idade = anoAtual-anoNasc
print(f"Olá {nome} você tem {idade} anos")