# Calcular a média e determinar a classificação de 3 notas dos alunos:
#   Se média entre : 8 e 10, classificação “A”; 
#   Se média entre: 7 e 7,9, classificação “B”; 
#   Se média entre: 5 e 6,9, classificação “C”; 
#   Se média abaixo de 5, classificação “D”. 
#   Mostrar como resultado: nome aluno, média, classificação

nome = input()
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
media = (nota1 + nota2 + nota3)/3
if(media>=8 and media<=10):
    classi = "A"
elif(media>=7 and media<=7.9):
    classi = "B"
elif(media>=5 and media<=6.9):
    classi = "C"
else:
    classi = "D"
print(f"O aluno {nome} obteve media igual a {media} e sua classificação final é {classi}")