# Calcular o fatorial de um valor lido pelo usuário. Exemplo: fatorial de 5. 
# Para o cálculo: 5! = 5 x 4x 3 x 2 x 1 Mostrar o resultado

num = int(input())
fatorial = 1
for i in range(num, 0, -1):
    fatorial *=i
print(fatorial)