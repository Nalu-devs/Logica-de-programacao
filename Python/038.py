# Ler os valores de um vetor inteiro de tamanho 10, e mostre o resultado da
# soma dos números ímpares presentes neste vetor.

vetor = []
soma = 0
for i in range(10):
    num = int(input())
    vetor.append(num)
    if num%2!=0:
        soma+=num
print(soma)