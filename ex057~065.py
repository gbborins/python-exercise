sexo = str(input("Qual o seu sexo?"))
while sexo != "M" and sexo != "F" and sexo != "m" and sexo != "f":
    sexo = str(input("Qual o seu sexo?"))
import random
numero = random.randint(0,10)
print("O computador digitou um numero entre 0 e 10")
seu = int(input("Qual o seu chute?"))
while numero != seu:
    print("Você errou o número")
    seu = int(input("Digite um número?"))
print(f"Você acertou o número é {numero}")
v1 = int(input("Digite um valor:"))
v2 = int(input("Digite outro valor"))
num = 0
while num != 5:
    if num == 1:
        print(f"A soma é:{v1+v2}")
    elif num == 2:
        print(f"A multiplicação é:{v1*v2}")
    elif num == 3:
        if v1 >= v2:
           print(f"Este número é maior{v1}")
        else:
            print(f"Este número é maior{v1}")
    elif num == 4:
        v1 = int(input("Digite um valor:"))
        v2 = int(input("Digite outro valor"))
    print('''[1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos números
      [5] Sair do programa''')
    num = int(input("Digite um valor:"))
valor = int(input("Digite um número:"))
i = 0
fatorial = 1
while i != valor:
    fatorial *= (valor-i)
    i+=1
print(f"{fatorial}")
fatorial2 = 1
for i in range(0,valor,1):
    fatorial2 *= (valor-i)
print(f"{fatorial2}")
termo1 = int(input("O primeiro termo é:"))
razao = int(input("A razão é:"))
i = 1
result = 0
while i != 11:
     result = termo1 +(i-1)*razao
     print(f"{result}")
     i+=1
quant = int(input("Quantos termo:"))
i = 1
while quant != 0:
    while quant+1 != i:
        result = termo1 +(i-1)*razao
        print(f"{result}")
        i +=1
    quant = int(input("Quantos termos:"))
    i = 1
ner = int(input("Digite quantos valores de Fibonacci"))
i = 0
soma = 0
soma2 = 1
print(f"0")
print(f"1")
if ner >2:
    while (ner-2) != i:
        soma = soma + soma2
        print(f"{soma}")
        troca = soma
        soma = soma2
        soma2 = troca
        i +=1
ve1 = int(input("Digite um número:"))
somat = ve1
cont = 0
while ve1 != 999:
    ve1 = int(input("Digite um número:"))
    somat += ve1
    cont += 1
print(f"A soma de todos os valores digitados é:{somat-999}")
print(f"A quantidades de número digitados foi {cont} ")
