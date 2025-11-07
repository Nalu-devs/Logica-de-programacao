# Faça um algoritmo que gere valores de 1 a 100 e calcule e envie para a média aritmética dos 
# valores gerados.

soma=0
cont=0
for i in range (1, 101):
    soma+=i
    cont+=1
    
media = soma/cont
print(f"A media é: {media:.2f}")