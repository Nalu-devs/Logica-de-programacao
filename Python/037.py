# Guardar em um vetor o ano de nascimento de 10 pessoas e gerar em outro vetor a idade de 
# cada pessoa. Mostrar como resultado o ano de nascimento e a idade calculada das 10 pessoas 
# e mostre qual a média das idades.

ano = []
idade = []
soma = 0
anoAtual = int(input("Digite o ano que estamos"))
for i in range(10):
    anoNasc = int(input())
    ano.append(anoNasc)
    idadeTodos = anoAtual-anoNasc
    idade.append(idadeTodos)
    soma+=idadeTodos
media=soma/10
print(ano)
print(idade)
print(media)