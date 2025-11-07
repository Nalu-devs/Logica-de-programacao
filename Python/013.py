# Faça um programa que mostre o nome do produto quanto vai ser seu custo (multiplicando a 
# quantidade pelo valor) e como vai ser sua forma de pagamento

nome = input()
quant = int(input())
valor = float(input())
custo = quant*valor
fp = input()
print(f"O produto {nome} vai ter custo de {custo} e a forma de pagamento {fp}")