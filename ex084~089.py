list = []
nome = str(input("Digite um nome:"))
peso = int(input("Digite uma peso:"))
list.append([nome,peso])
i = 1
peso_menor = peso
peso_maior = peso
nome_menor_peso = []
nome_maior_peso = []
word = str(input("Você quer continuar s/n:"))
while word.lower() != 'n':
    nome = str(input("Digite um nome:"))
    peso = int(input("Digite uma peso:"))
    list.append([nome,peso])
    i += 1
    word = str(input("Você quer continuar s/n:"))
    if peso >= peso_maior:
        peso_maior = peso
    if peso <= peso_menor:
        peso_menor = peso
for j in list:
    if j[1] == peso_maior:
        nome_maior_peso.append(j[0])
    if j[1] == peso_menor:
        nome_menor_peso.append(j[0])
print(f"Você cadastrou {i} pessoas")
print(f"O maior peso foi {peso_maior}. Peso de {nome_maior_peso}")
print(f"O maior peso foi {peso_menor}. Peso de {nome_menor_peso}")
lista = []
lista.append([])
lista.append([])
for i in range(0,7):
    num = int(input(f"Digite o {i+1}° número:"))
    if num%2 == 0:
        lista[0].append(num)
    elif num%2 != 0:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f"Os pares em ordem crescente são: {lista[0]}")
print(f"Os impares em ordem crescente são: {lista[1]}")
#exer 86
lists = []
for i in range(0,3):
    lists.append([])     
    for j in range(0,3):
        num = int(input(f"Digite o valor da posição [{i,j}]"))
        lists[i].append(num)
for k in range(0,3):
    for l in range(0,3):
        print(f"[ {lists[k][l]} ]", end = " ")
        if l == 2:
            print("\n")
#exer 87
lists = []
par = 0
coluna_3 = 0
maior_2linha = 0
for i in range(0,3):
    lists.append([])     
    for j in range(0,3):
        num = int(input(f"Digite o valor da posição [{i,j}]"))
        if num % 2 == 0:
            par += num
        if j == 2:
            coluna_3 += num
        if i == 1 and num >= maior_2linha:
            maior_2linha = num
        lists[i].append(num)
for k in range(0,3):
    for l in range(0,3):
        print(f"[ {lists[k][l]} ]", end = " ")
        if l == 2:
            print("\n")
print(f"A soma dos pares são:{par}")
print(f"A soma dos valores da terceira coluna são:{coluna_3}")
print(f"O maior valor da segunda linha são: {maior_2linha}")
#exer 88
import random
list_sorteio = []
num_jogos = int(input("Quantos jogos serão gerados?"))
for i in range(0,num_jogos):
    list_sorteio.append([])
    for j in range(0,6):
        list_sorteio[i].append(random.randint(0,60))
for i, j in enumerate(list_sorteio):
    print(f"O jogo {i+1}: {j}")
#exer 89
word = ''
list_alunos = []
num_aluno = 0
while word.lower() != 'n':
    nome = str(input("Digite seu nome:"))
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a secunda nota:"))
    list_alunos.append([nome,nota1,nota2])
    word = str(input("Você quer continuar?"))
for j,i in enumerate(list_alunos):
    print(f"N°{j} e nome {i[0]} e anota {(i[1]+i[2])/2}")
while num_aluno != 999:
    num_aluno = int(input("Digitar a nota de qual aluno? (999 interrompe)"))
    nome = list_alunos[num_aluno][0]
    nota1 = list_alunos[num_aluno][1]
    nota2 = list_alunos[num_aluno][2]
    print(f"As notas de {nome} são: {nota1} e {nota2} ")