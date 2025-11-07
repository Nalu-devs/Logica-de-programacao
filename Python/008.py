# Indique o valor do salário e o percentual de aumento, calcule o valor do reajuste

sal = float(input())
reajuste = float(input("em %"))
salFinal = (sal*(reajuste/100))+sal
print(salFinal)