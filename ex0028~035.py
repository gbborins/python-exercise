import random
num = random.randint(0,5)
res = int(input('Adivinhe qual número o computador escolheu de 0 a 5, digite o número:'))
if 0 < res <= 5:
    if res == num:
        print(f'Meu parabéns você acertou o número foi {num}')
    else:
        print(f'você errou o número foi {num}')
else:
    print('você tem que digitar um número entre 0 e 5')
vel = int(input('Digite a velocidade de um carro:'))
if vel > 80:
    print('você foi mutado')
    multa = (vel-80)*7
    print(f'a multa vai custa R${multa}')
parim = int(input('Digite um número:'))
div = parim/2
if int(div) == div:
    print('Seu número é par')
else:
    print('Seu número é impar')
via = float(input('A distância da viagem:'))
if via <= 200:
    via50 = via*0.5
    print(f'O preço da viagem vai sair {via50}')
else: 
    via45 = via*0.45
    print(f'O preço da viagem vai sair {via45}')
ano = int(input('Digite um ano:'))
bises = ano/4
if int(bises) == bises:
    print('Esse ano é ano bissexto')
else:
    print('Não é um ano bissexto')
num1 = int(input('Digite um número:'))
num2 = int(input('Digite um número:'))
num3 = int(input('Digite um número:'))
nums = [num1,num2,num3]
print(f'O maior número é {max(nums)}')
print(f'O menor número foi {min(nums)}')
sal = float(input('Digite seu salário:'))
if sal > 1250:
    print(f'Seu novo salário será {sal+(sal*0.10)}')
else:
    print(f'Seu novo salário será {sal+(sal*0.15)}')
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a<(b+c) and a>(b-c) and b<(a+c) and b>(a-c) and c<(a+b) and c>(a-b) :
	print('O triangulo pode existir')
else:
	print('O triangulo nao pode existir!!!')