# Ler os valores para nome, peso e altura de uma pessoa e calcular o seu IMC (índice de massa 
# corporal) pela fórmula: IMC = peso/(altura2) Escrever o nome da pessoa, seu imc e sua classificação 
# de acordo com a tabela:
#   Se o resultado do IMC for até 18, escrever “baixo peso” 
#   Se for maior que 18 e menor igual a 24, escrever “normal”
#   Se for maior que 24, escrever ‘Obeso’.

nome = input()
peso = float(input())
altura = float(input())
imc = peso/(altura**2)
if(imc<=18):
    classificacao = "Baixo peso"
elif(imc>18 and imc<=24):
    classificacao = "Normal"
else:
    classificacao = "Obeso"
print(f"{nome} seu imc é igual a {imc} e se classifica como {classificacao}")