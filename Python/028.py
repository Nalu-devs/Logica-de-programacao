# Programa que calcula a divisão de um número pelo outro, sabendo que o quociente tem que ser 
# diferente de 0

num = int(input())
num2 = int(input())
if(num2 == 0):
    print("Divisão impossivel")
else:
    res = num/num2
    print(f"Resultado: {res}")