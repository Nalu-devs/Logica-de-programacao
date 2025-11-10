# Guardar 20 valores reais em um vetor e mostrar todos os valores guardados nas posições pares 
# (2-20). Não se esqueça que o índice começa em zero.

vetor = []
novoVetor = []
for i in range(20):
    num = int(input())
    vetor.append(num)
    if i%2==0:
        novoVetor.append(num)
print(novoVetor)