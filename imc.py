# Programa para calcular IMC
# Desenvolvido por Tamires

print ("**************************************************")
print ("*                CALCULADORA DE IMC              *")
print ("**************************************************")
print ()

#Criação das Variáveis

nome = ""
peso = 0
altura = 0.0
imc = 0.0

#Entrada dos dados

nome= input(" Digite o seu nome: ")
peso= int(input(" Digite o seu peso: "))
altura= float(input(" Digite a sua altura: "))

# Processar os valores para obter o IMC
              
imc= peso / altura ** 2

# Saída do processamento

print()
print("***********************************************")
print("*****************RESULTADO*********************")
print("***********************************************")
print("*                                             *")
print("Nome: " + nome )
print("Peso: " + str(peso) + " Kg ")
print("Altura: " + str(altura) + " m ")
print("IMC: " + str(imc))

if imc < 18.5:
    situacao= "abaixo do peso"
elif imc >= 18.5 and imc <25:
    situacao= "com peso normal"
elif imc >= 25 and imc <30:
    situacao= "com sobrepeso"
elif imc >= 30 and imc <35:
    situacao= "com obesidade grau I"
elif imc >= 35 and imc <40:
    situacao= "com obesidade grau II"
else:
    situacao= "com obesidade Grau III ou Mórbida"

print(f" {nome}, você está {situacao}.")


