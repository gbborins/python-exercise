#Exer101
from datetime import datetime
def voto(ano):
    if idade >= 65 :
        return "Voto Opcional"
    elif idade >= 18:
        return "Voto Obrigátório"
    else:
        return "Voto Negado"
idade = datetime.now().year - int(input("Digite ano de nascimento: "))
print(f"Com {idade} anos: {voto(idade)}")
#Exer102
def fatorial(numero, show = False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fact = 1
    for i in range(numero,0,-1):
        if show == True:
            print(f"{i}", end ="" )
            if i != 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        fact *= i
    return fact
numero = int(input("Número a ser fatorado: "))
show = str(input("Mostrar o processo ou não True/False: "))
if show == '' or show == 'False':
    show = False
elif show == 'True':
    show = True
else:
    print('Erro do processo')
print(fatorial(numero,show))
#Exer103
def ficha(nome = '<desconhecio>', gols = 0):
    gols = int(gols)
    print(f"O jogador {nome} fez {gols}(s) no campeanato.")
jogador = str(input("Nome do jogador: "))
gols = str(input("Número de Gols: "))
if jogador == '' or gols == '':
    if jogador != '':
        ficha(jogador)
    elif gols != '':
        ficha(gols = gols)
    else:
        ficha()     
else:
    ficha(jogador,gols)
#exer104
def leiaInt(valor):
    num = input(valor)
    while True:
        if num in '0987654321' and num != '':
            break   
        else:
            print(f"Erro! Digite um número inteiro válido")
        num = input(valor)
    return num
n = leiaInt('Digite um número: ')
print(f"Você acabou de digitar o número {n}")
#Exer105
def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situacao.
    :return: dicionário com várias informacoes sobre a situacao da turma.
    """
    notas = {}
    notas['total'] = len(num)
    notas['maior'] = max(num)
    notas['menor'] = min(num)
    notas['media'] = sum(num)/len(num)
    if sit == True:
        if notas['media'] >= 6:
            notas['situacao'] = 'Aprovado'
        else:
            notas['situacao'] = 'Reprovado'
    return notas
word = list(map(float, input("Digite as notas separadas por espaço: ").split()))
situ = str(input("Mostrar a situação ou não, True/False: "))
if situ == '' or situ == 'False':
    situ = False
elif situ == 'True':
    situ = True
else:
    print('Erro do processo')
res = notas(*word,sit = situ)
print(res)