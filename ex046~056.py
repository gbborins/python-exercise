for c in range (11,1,-1):
    print(c-1)
    print("")
print("fim")
for n in range (0,51,2):
    print(n)
print("fim")
soma = 0
for h in range(0,500,3):
    if h%2 == 1:
        soma += h
print(soma)
print("fim")
num = int(input("Digite um número:"))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
sum = 0
for i in range(0,6):
    num = int(input("Digite um número:"))
    if(num%2 == 0):
        sum +=num 
print(f"A soma é dos pares é {sum}")
termo1 = int(input("Qual o primeiro termo?"))
razao = int(input("Qual a razão da PA?"))
for i in range(10,0,-1):
    termo = termo1 + razao*(10-i)
    print(termo)
cont = 0
nu = int(input("Escreva um número inteiro:"))
for i in range(2,999):
    if nu%i == 0 :
        cont +=1
if cont >= 2:
    print("Não é um número primo")
else:
    print("É um número primo ")
frase = str(input("Digite uma frase"))
frase = frase.replace(" ", "").lower()
frasen = frase[::-1]
if frasen == frase:
    print("É um palindromo")
else:
    print("Não é um palindromo")
num = 0
for i in range(1,8,1):
    idade= int(input("Digite seu ano de nascimento"))
    if (2025-idade) >= 18:
        num += 1
print(f"A quantidade que atingiu a maioridade é {num}")
print(f"A quantidade que não atingiu a maioridade é {7-num}")
grande = float(input("Digite seu peso?"))
maior = grande
menor = grande
for i in range(1,5,1):
    grande = float(input("Digite seu peso?"))
    if(grande >= maior):
        maior = grande
    if(grande <= menor):
        menor = grande
print(f"O maior número é: {maior}")
print(f"O maior número é: {menor}")
nome = str(input("Qual seu nome?"))
idade = int(input("Qual sua idade?"))
sexo = str(input("Qual seu sexo?"))
mendia = idade
idadevelho = idade
hovelho = nome
mu20 = 0
for i in range(1,4,1):
    nome = str(input("Qual seu nome?"))
    idade = int(input("Qual sua idade?"))
    sexo = str(input("Qual seu sexo?"))
    if sexo == 'm' and idade <20:
        mu20 +=1
    if(idade >= idadevelho and sexo == 'h'):
        hovelho = nome
        idade = idadevelho
    mendia += idade
mendia /= 4
print(f"A idade média do grupo é: {mendia}")
print(f"O nome do homem mais velho é: {hovelho}")
print(f"A quantidade de mulher que tem menos de 20 anos são: {mu20}")