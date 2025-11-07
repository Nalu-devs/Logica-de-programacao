# Peça ao usuário para digitar a velocidade maxima permitida em uma pista e a velocidade que 
# ele estava dirigindo:
#   Se o motorista passou até 10 paga multa de 50
#   Se passou de 11 a 30 multa de 100
#   Se passou acima de 30 multa de 200
#   Se não sem multa
vm = int(input())
vd = int(input())
if(vd>vm):
    dife = vd-vm
    if(dife<=10):
        multa = 50
    elif(dife>=11 and dife<=30):
        multa = 100
    elif(dife>30):
        multa = 200
else:
    multa = 0
print(f"O valor da multa a pagar é R${multa}")