# Peça ao usuário a duração de um evento e informe as horas, minutos e segundos desse tempo

de = int(input())
h = de//3600
m = (de%3600//60)
s = (de%60)
print(f"O evento durou: {h} Horas {m} Minutos e {s} Segundos")