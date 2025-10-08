um = int(input("Digite um número:"))
um2 = int(input("Digite um número:"))
um3 = int(input("Digite um número:"))
um4 = int(input("Digite um número:"))
um5 = int(input("Digite um número:"))
lista = (um,um2,um3,um4,um5)
maior = um
menor = um
for i in lista:
    if i >= maior:
        maior = i
    if i <= menor:
        menor = i
print(f"O maior número é {maior} e a posição é {lista.index(maior)+1} e o menor é {menor} e a posição é {lista.index(menor)+1}")
adicionar = ''
list = []
i = 0
while adicionar.lower() != 'n':
    num = int(input("Digite um número:"))
    if list.count(num) == 0:
        list.append(num)
    i += 1
    adicionar = str(input("Quer continuar S/N"))
list.sort()
print(f"{list}")
listed = []
for j in range(0,5):
    tar = int(input("Digite um número:"))
    if not listed or tar > listed[-1]:
        listed.append(tar)
    else:
        for i,val in enumerate(listed):
            if tar <= val:
                listed.insert(i,tar)
                break
    print(f"Lista atual:{listed} e está na posição {listed.index(tar)}")
print(f'A seguência é {listed}')
ans = ''
cont = 0
lent = []
while ans.lower() != 'n':
    word = int(input("Digite um número:"))
    ans = str(input("Quer continuar S/N"))
    cont+=1
    lent.append(word)
print(f"Fora digitados {cont} números")
lent.sort(reverse=True)
print(f"Os valores são{lent}")
if lent.count(5) != 0:
    print("O valor 5 está contido")
else:
    print("O valor 5 não está contido")
ans = ''
lent = []
lentpar = []
lentimpar = []
while ans.lower() != 'n':
    num = int(input("Digite um número:"))
    ans = str(input("Quer continuar S/N"))
    lent.append(num)
    if num%2 == 0:
        lentpar.append(num)
    else:
        lentimpar.append(num)
print(f"Os valores são{lent}")
print(f"Os valores pares são{lentpar}")
print(f"Os valores impares são{lentimpar}")
