# Ler o nome, a quantidade adquirida e o preço unitário. Calcular e escrever o total a pagar. Onde:
#   Total = quantidade adquirida * preço unitáritotal
#   Pagar = total – desconto
#   O desconto será calculado, sabendo-se que:
#   - Se quantidade <= 20 o desconto será de 2%
#   - Se quantidade > 20 o desconto será de 5%
# OBS: quantidade máxima permitida é 50 (não aceitar valores superiores).

nome = input()
quant = int(input())
precoUni = float(input())
total = quant * precoUni

if(quant>50):
    print("Quantidade maxima é 50")
else:
    if(quant <= 20):
        desconto = 0.02
    elif(quant > 20 and quant<=50):
        desconto = 0.05
pagar = total-(total * desconto)
print(f"O valor final do {nome} é R${pagar:.2f}")