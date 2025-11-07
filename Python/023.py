# Escrever um programa que leia uma sequência de valores inteiros, até ser lido o valor -99. 
# Quando isso acontecer o programa deverá mostrar a soma e a média dos valores lidos.

soma = 0
cont = 0
while True:
    num = float(input())
    if(num == -99):
        break
    soma += num
    cont += 1
media = soma/cont
print(f"Soma: {soma}\nMedia: {media:.2f}")