# Fazer um programa no qual o usuário entrará sucessivamente com valores positivos. 
# Quando o usuário entra com um valor negativo o programa para pedir valores e calcular a 
# média dos valores já fornecidos.

soma = 0
cont = 0
while True:
    num=int(input())
    if(num<0):
        break
    soma += num
    cont += 1
media = soma/cont
print(f"A media é {media}")