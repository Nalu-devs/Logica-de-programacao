# Ler o nome, o salário fixo e o valor das vendas efetuadas pelo vendedor de uma loja. Sabendo-se que:
#   Recebe uma comissão de 3% sobre o total das vendas até R$ 2.000,00
#   Recebe 5% sobre vendas acima de R$ 2.000,00 e R$ 5.000,00 e
#   Recebe 10% para vendas acima de R$ 5000,00
# Calcular e escrever o seu nome e o salário com abono.
nome = input()
salFixo = float(input())
venda = float(input())
if(venda<=2000):
    comis = 0.03
elif(venda>2000 and venda<=5000):
    comis = 0.05
else:
    comis = 0.1
salFinal = salFixo + (venda*comis)
print(f"O vendedor {nome} receberá de salario {salFinal:.2f}")