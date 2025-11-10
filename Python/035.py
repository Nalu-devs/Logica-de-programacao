# Guardar 20 valores inteiros em um vetor e mostrar como resultado: Se o valor for positivo, 
# seu dobro, se o valor negativo, seu positivo correspondente.

vetor = []
novoVetor = []
for i in range(20):
    num = int(input())
    vetor.append(num)
    if num>0:
        dobro = num*2
        novoVetor.append(dobro)
    else:
        positivo = num*-1
        novoVetor.append(positivo)
print(novoVetor)