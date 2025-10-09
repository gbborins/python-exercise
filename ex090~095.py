#ex 90
aluno = {}
aluno['nome'] = str(input("Digite o nome:"))
aluno['media'] = float(input("Digite a media:"))
if aluno['media'] >= 6.0:
    aluno['situacao'] = "Aprovado"
elif aluno['media'] < 6.0:
    aluno['situacao'] = "Reprovado"
print(f"O nome é igual a {aluno['nome']}")
print(f"A media é igual a {aluno['media']}")
print(f"O situacao é igual a {aluno['situacao']}")
#ex 91
import random
import time
import operator
''' from random import randint
from time import sleep
from operator import itemgetter
'''
dado = {}
dado_org = {}
for i in range(1,5):
    ran = random.randint(0,6)
    dado[f"jogador{i}"] = ran
    print(f'O jogador{i} tirou {ran}')
    time.sleep(1)
dado_org = sorted(dado.items(), key = operator.itemgetter(1),reverse = True)
# dado_org = sorted(dado.tems(), key= lambda item: item[1], reverse=True)[0]
for i,j in enumerate(dado_org):
    print(f"O {i+1}°lugar foi o {dado_org[i][0]} com o valor {dado_org[i][1]}")
#Exer 92
from datetime import datetime
usua = {}
usua['nome'] = str(input('Nome: '))
usua['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
usua['trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if usua['trabalho'] != 0:
    usua['ano de contração'] = int(input("Ano de contratação: "))
    usua['salario'] = float(input("Salário: "))
    usua['aposentar'] = usua['idade'] + usua['ano de contração'] + 35 - datetime.now().year
print(usua)
for k,v in usua.items():
    print(f"{k} é {v}")
#Exer 93
jogo = {}
jogo['nome'] = str(input("Nome do jogador: "))
quant = int(input(f"Quantas partidas {jogo['nome']} jogou? "))
i = 0
total = 0
jogo['partida'] = []
while quant > 0:
    jogo['partida'].append(int(input(f"Quantos gols na partida {i+1}: ")))
    quant -= 1
    i += 1
print(f"O jogador {jogo['nome']} jogou {i} partidas")
for j,k in enumerate(jogo['partida']):
    print(f"Na partida {j}, fez {k} gols")
    total += k
jogo['total'] = total
print(f"Foram {jogo['total']} gols")
#Exer 94
pes = ''
list = []
cont = 0
media = 0
mulheres = []
up = []
while True:
    if pes.lower() == 'n':
        break
    nome = str(input("Qual seu nome? "))
    sexo = str(input("Qual seu sexo M/F: "))
    idade = int(input("Qual sua idade? "))
    list.append({'nome': nome, 'sexo':sexo, 'idade': idade})
    pes = str(input("Quer continuar (N)/(S): "))
    media += list[cont]['idade']
    cont += 1
media /= cont
for j,i in enumerate(list):
    if i['sexo'].lower() == 'f':
        mulheres.append(list[j]['nome'])
    if i['idade'] > media:
        up.append(list[j])
print(f"Foram contratadas {cont} pessoas")
print(f"A média de idade é {media}")
print(f"A lista com todas as mulheres são {mulheres}")
print(f"As pessoas acima da media são {up}")