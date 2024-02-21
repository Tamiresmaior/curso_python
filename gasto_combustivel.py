# Programa para calcular o custo de combustivel gasto em X viagem
# Desenvolvido por Tamires


print("*********************************************")
print("**********CONSUMO DE COMBUSTÍVEL*************")
print("*********************************************")

#Criação das Variáveis

modelo_carro: ""
autonomia_do_carro: 0
distancia_do_carro: 0
preço_do_combustivel: 0.0
combustivel_utilizado: 0.0
gasto_com_combustivel_na_viagem: 0.0

#Entrada dos dados

modelo_carro = input( " Qual o modelo do veículo? ")
autonomia_do_carro = int(input( " Qual a autonomia do veículo? " ))
distancia_do_carro = int(input( " Qual a distância da viagem?" ))
preço_do_combustivel = float(input( " Qual o preço do combustível? "))

# Processar os valores 

combustivel_utilizado = distancia_do_carro / autonomia_do_carro
gasto_com_combustivel_na_viagem = combustivel_utilizado * preço_do_combustivel

# Saída do processamento

print()
print("***********************************************")
print("******************RESULTADO********************")
print("***********************************************")
print("*                                             *")
print(f" Modelo do veículo: {modelo_carro} " )
print(f" Autonomia do veículo: {autonomia_do_carro} Km/l")
print(f" Distancia percorrida: {distancia_do_carro} Km")
print(f" Valor do combustível: R$ {preço_do_combustivel}")

print()
print("***********************************************")
print(f" Quantidade de combustível utilizado: {combustivel_utilizado:.2f}l")
print(f" Total gasto com a viagem: R$ {gasto_com_combustivel_na_viagem:.2f}")


                                   






    
