# Guardar 10 valores inteiros e positivos em um vetor e gerar outro vetor com resultados da 
# seguinte forma: Se o valor guardado for par, multiplica-lo por 2, se o valor guardado for 
# ímpar, multiplica-lo por -1.

vetorPositivo = []
vetorDiferente = []
for i in range(10):
    num = int(input())
    if num>0:
        vetorPositivo.append(num)
    if num%2==0:
        dobro = num*2
        vetorDiferente.append(dobro)
    else:
        negativo = num*-1
        vetorDiferente.append(negativo)
print(vetorPositivo)
print(vetorDiferente)