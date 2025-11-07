# Solicite a idade de várias pessoas e imprima: Quantidade de pessoas com menos de 21 anos. 
# Quantidade de pessoas com mais de 50 anos. O programa termina quando idade digitada for -99

cont21 = 0
cont50 = 0
while True:
    idade = int(input())
    if(idade == -99):
        break
    elif(idade<21):
        cont21 += 1
    elif(idade>50):
        cont50 += 1
print(f"Pessoas com menos de 21 {cont21}\n Pessoas com mais de 50 {cont50}")