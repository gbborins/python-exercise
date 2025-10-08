n = 0
sum = 0
while True:
    v1 = int(input("Digite um número:"))
    if v1 == 999:
        break
    sum += v1
    n += 1
print(f"A quantidade é:{n}")
print(f"A soma é:{sum}")
num = int(input("Digite um número para fazer tabuada:"))
i = 1
while True:
    if num <0:
        break
    while i<=10:
        print(f"{num}x {i} = {num*i}")
        i +=1
    num = int(input("Digite um número para fazer tabuada:"))
    i =0
import random
parimpar = random.randint(0,10)
cont = 0
dois = 0
while True:
    dig = str(input("Par ou Impar?, p/i"))
    n1 = int(input("Mostre um número:"))
    print(f"{parimpar}")
    dois = parimpar + n1
    print(f"{dois}")
    if dois%2 == 1:
        if dig == "i":
            print("Você ganhou")
            parimpar = random.randint(0,10)
            dig = str(input("Par ou Impar?"))
            n1 = int(input("Mostre um número:"))
            cont +=1
        else:
            print(f"Você perdeu sua sequencia foi:{cont}")
            break
    else:
        if dig == "p":
            print("Você ganhou")
            parimpar = random.randint(0,10)
            dig = str(input("Par ou Impar?"))
            n1 = int(input("Mostre um número:"))
            cont +=1
        else:
            print(f"Você perdeu sua sequencia foi:{cont}")
            break
dezoito = 0
homens = 0
mulher2 = 0
while True:
    id = int(input("Qual a sua idade:"))
    sex = str(input("Qual o seu gênero: h/m"))
    if id > 18:
        dezoito += 1
    if sex == "h":
        homens += 1
    if sex == "m" and id < 20:
        mulher2 += 1
    continuar = str(input("Quer continuar s/n"))
    if continuar == "n":
        break
print(f"As pessoas que tem mais de 18 são:{dezoito}")
print(f"A quantidade de homens cadastrados são:{homens}")
print(f"As mulheres que tem menos de dezoito são:{mulher2}")
prod = str(input("Qual o nome do produto:"))
preço = float(input("O quanto vale seu produto:"))
soma = preço
nomebarato = prod
barato = preço
if preço > 1000:
    mais1000 = 1
else:
    mais1000 = 0
while True:
    prod = str(input("Qual o nome do produto:"))
    preço = float(input("O quanto vale seu produto:"))
    if preço > 1000:
        mais1000+= 1
    soma += preço
    if preço < barato:
        nomebarato = prod
    continua = str(input("Continuar s/n"))
    if continua == "n":
        break
print(f"Foi gasto na soma total:{soma}")
print(f"Os produtos que custam mais de 1000 são:{mais1000}")
print(f"O nome do produto mais barato é:{nomebarato}")
valor = int(input("O valor a ser sacado é:"))
comp = valor
n50 = 0
n20 = 0
n10 = 0
n1 = 0
while True:
    if comp >= 50:
        comp -= 50
        n50 += 1
    else:
        break
while True:
    if comp >= 20:
        comp -= 20
        n20 += 1
    else:
        break
while True:
    if comp >= 10:
        comp -= 10
        n10 += 1
    else:
        break
while True:
    if comp > 0:
        comp -= 1
        n1 += 1
    else:
        break
print(f"Seram entregues {n50} de cinquenta")
print(f"Seram entregues {n20} de vinte")
print(f"Seram entregues {n10} de dez")
print(f"Seram entregues {n1} de um")