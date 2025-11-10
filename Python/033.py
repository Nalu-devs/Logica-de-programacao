# Criar um vetor, preenchê-lo com valores fornecidos pelo usuário e depois imprimi-los.

vetor = []
while True:
    num=int(input())
    if num == -1:
        break
    vetor.append(num)
print(vetor)