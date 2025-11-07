# Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo 
# que permita a entrada das seguintes informações:
#   a. o número total de mercadorias no estoque;
#   b. o valor de cada mercadoria
# Ao final imprimir o valor total em estoque e a média de valor das mercadorias.

totalEstoque = int(input())
soma = 0
cont = 0
for i in range (totalEstoque, 0, -1):
    valor=float(input())
    soma+=valor
    cont+=1

media=soma/cont
print(f"Valor total em estoque {soma} e media {media}")