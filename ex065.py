val1 = float(input("Digite um número:"))
sum = val1
cont = 1
maior = val1
menor = val1
rodar = "s"
while rodar == "s":
    val1 = float(input("Digite um número:"))
    sum += val1
    cont += 1
    if val1 >= maior:
        maior = val1
    if val1 <= menor:
        menor = val1
    rodar = str(input("Quer continuar s/n"))
print(f"A media é{sum/cont}")
print(f"O maior número lido é {maior}")
print(f"O menor número lido é {menor}")
