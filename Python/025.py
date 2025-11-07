# Escrever um programa que recebe vários números inteiros no teclado. E no final imprimir a 
# média dos números múltiplos de 3. Para sair digite 0 (zero)

soma = 0
cont3 = 0
while True:
    num = int(input())
    if(num == 0):
        break
    elif(num%3==0):
        cont3 += 1
        soma +=num
media = soma/cont3
print(f"A media dos multiplos de 3 é: {media}")