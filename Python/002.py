# Peça ao usuário que digite o ano, o mes e o dia que nasceu e calcule a idade dele apenas em dias

ano = int(input())
anoAtual = int(input())
mes = int(input())
mesAtual = int(input())
dia = int(input())
diaAtual = int(input())
apenasDias = ((anoAtual*365)+(mesAtual*30)+diaAtual)-((ano*365)+(mes*30)+dia)
print(apenasDias)