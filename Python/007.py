# Indique o valor do salário e do aumento e calcule o valor do reajuste

sal = float(input())
reajuste = float(input("em %"))
salFinal = (sal*(reajuste/100))+sal
print(salFinal)