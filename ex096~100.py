#Exer 96
def area(largura, comprimento):
    print(f"A área de um terreno {largura}x{comprimento} é de {largura*comprimento}m²")
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)
#Exer 97
def escreva(texto):
    print('~', end='')
    for i in texto:
        print('~', end='')
    print('~')
    print(f" {''.join(texto)} ")
    print('~', end='')
    for i in texto:
        print('~', end='')
    print('~')
escreva(list(str(input())))
#Exer 98
import time
def contador(inicio,fim,passo):
    if passo > 0:
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    elif passo == 0:
        passo = 1
    else:
        print(f"Contagem de {inicio} até {fim} de {passo*-1} em {passo*-1}")
    if fim < inicio:
        if passo > 0:
            passo *= -1
        fim -= 1
    else:
        fim += 1
    for i in range(inicio,fim,passo):
        time.sleep(0.5)
        print(f'{i} ',end='', flush = True)
    print('')
contador(1,10,1)
contador(10,0,2)
print("Personalize a contagem")
inicio = int(input("Início: "))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
#Exer 99
def maior(listed):
    print("Analisando os valores passado...")
    tam = len(listed)
    maior = listed[0]
    for i in listed:
        print(f'{i} ',end='', flush = True)
        time.sleep(0.5)
        if i > maior:
            maior = i
    print(f"\n Foram informado {tam} valores ao todo")
    print(f"O maior valor informado foi {maior}")
listed = []
num = 1
while True:
    num = int(input())
    listed.append(num)
    if num == 0:
        break
maior(listed)
#Exer 100
from random import randint
def sorteia():
    print(f"Sorteando 5 valores da lista: ", end= '')
    numeros = []
    for i in range(0,5):
        ale = randint(0,10)
        numeros.append(ale)
        print(f"{ale} ", end='', flush = True)
        time.sleep(0.5)
    print('PRONTO!')
    somaPar(numeros)
def somaPar(numeros):
    sum = 0
    for j in numeros:
        if j%2 == 0:
            sum += j
    print(f"Somando os valores pares de {numeros}, temos {sum}")
sorteia()