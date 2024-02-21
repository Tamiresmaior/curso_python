("*************************************")
("********TIPOS DE TRIÂNGULOS**********")
("")


lado_a = 0.0
lado_b = 0.0
lado_c = 0.0


lado_a = int(input(" Digite o lado a do triângulo: "))
lado_b = int(input(" Digite o lado b do triângulo: "))
lado_c = int(input(" Digite o lado c do triângulo: "))

situacao = ""

if (lado_a == lado_b) and (lado_a == lado_c):
    situacao = "EQUILÁTERO"
    
elif lado_a != lado_b != lado_c:
    situacao = "ESCALENO"
    
else:
    situacao = "ISÓSCELES"

print("Esse triângulo é um {situacao}.")

    
