# Programa para calcular Média Final
# Desenvolvido por Tamires


print ("*****************************")
print ()
print ("*CALCULADORA DE MEDIA FINAL**")
print ()
print ("*****************************")

#Criação das Variáveis

nome_do_aluno = ""
nota_bimestre_1 = 0.0
nota_bimestre_2 = 0.0
nota_bimestre_3 = 0.0
nota_bimestre_4 = 0.0
media_final = 0.0

#Entrada dos dados

nome_do_aluno = input (" Qual o nome do aluno? ")
nota_bimestre_1 = float(input(" Qual foi a sua nota no primeiro bimestre? "))
nota_bimestre_2 = float(input(" Qual foi a sua nota no segundo bimestre? "))
nota_bimestre_3 = float(input(" Qual foi a sua nota no terceiro bimestre? "))
nota_bimestre_4 = float(input(" Qual foi a sua nota no quarto bimestre? "))


# Processar os valores 

media_final = ((nota_bimestre_1 + nota_bimestre_2 + nota_bimestre_3 + nota_bimestre_4) / 4)

# Saída do processamento

#Verificar a situação

situação = ""

if media_final >=7.0:
    situação = "APROVADO"
  
elif media_final <5.0:
     situação = "REPROVADO"
     
else:
    situação = "em RECUPERAÇÃO"

#Exibir o resultado

print(f" {nome_do_aluno}, você está {situação}, com média {media_final}. ")
     

