# Peça ao usuário para digitar três numeros e diga o valor de D sabendo que:
#   R=(a+b)/c
#   S=(b+c)/a
#   D=(r+s)/2
a = float(input())
b = float(input())
c = float(input())
r = (a+b)/c
s = (b+c)/a
d = (r+s)/2
print(d)