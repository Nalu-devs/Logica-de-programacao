# Crie um algoritmo que leia uma senha fornecida pelo usuário composta por caracteres para 
# informar se a senha é válida ou inválida. A senha do sistema corresponde a palavra “PORTUGOL”.

senha = "PORTUGOL"
tentativas = 0
while True:
    senhaUser = input()
    tentativas +=1
    if(senhaUser == "PORTUGOL"):
        print("Acertou a senha")
        break
    else:
        print("Senha inválida")
print(f"Você tentou por {tentativas} vezes")