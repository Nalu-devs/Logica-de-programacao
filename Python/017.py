# Gerar a tabuada de um valor solicitado pelo usuário e verificar se ele deseja novo 
# cálculo de tabuada

while True:
    num = int(input())
    for i in range (1, 11):
        res=num*i
        print(f"{num} X {i} = {res}")
    novoCal = input("Deseja fazer novo calculo? S/N")
    if(novoCal == "N"):
        break