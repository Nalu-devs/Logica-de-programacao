# Peça ao usuário para digitar três numeros e indique se a soma do segundo pelo terceiro é maior 
# ou menor que o primeiro

num1 = float(input())
num2 = float(input())
num3 = float(input())

if(num2+num3>num1):
    print(f"A soma de {num2} e {num3} é maior que {num1}")
else:
    print(f"A soma de {num2} e {num3} é menor que {num1}")