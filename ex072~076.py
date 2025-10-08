tuplanum = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero = int(input("Digite um número de 0 e 20:"))
while numero < 0 or numero > 20:
    numero = int(input("Tente novamente. Digite um número de 0 e 20:"))
print(f"Você digitou o número {tuplanum[numero]}")
colocados = ('Palmeiras','3','4','5','6','7','8','9','10','11','Chapecoense','12','13','14','15','16','17','18','19','20')
print(f"{colocados[:5]}")
print(f"{colocados[16:]}")
print(f"{sorted(colocados)}")
print(f"O Chapecoense está na posição {colocados.index('Chapecoense')+1}°")
import random
ale = random.randint(0,9999)
ale1 = random.randint(0,9999)
ale2 = random.randint(0,9999)
ale3 = random.randint(0,9999)
ale4 = random.randint(0,9999)
maior = ale
menor = ale
tupla = (ale,ale1,ale2,ale3,ale4)
print(tupla)
for aleMaior in tupla:
    if aleMaior >= maior:
        maior = aleMaior
for aleMenor in tupla:
    if aleMenor <= menor:
        menor = aleMenor
print(menor)
print(maior)
valor1 = int(input("Digite um valor:"))
valor2 = int(input("Digite um valor:"))
valor3 = int(input("Digite um valor:"))
valor4 = int(input("Digite um valor:"))
ruta = (valor1,valor2,valor3,valor4)
if 9 in ruta:
    print(f"a contagem de nove é:{ruta.count(9)}")
if 3 in ruta:
    print(f"A posição do numero três é {ruta.index(3)+1}")
for valor in ruta:
    if valor%2 == 0:
        print(f"O valor {valor} é par")
#Não vou fazer o 76