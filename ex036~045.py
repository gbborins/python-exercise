valor = float(input("Qual é o valor da casa?"))
salario = float(input("Qual o seu salário?"))
tempo = float(input("Em quantos anos você vai pagar?"))
prestação = valor/(tempo*12)
if (salario*30/100) < prestação:
    print("seu empréstimo foi negado")
else:
    print(f"Seu empréstimo mensal é de {prestação}")
número = int(input("Digite um número?"))
conversao = int(input("Qual será a base da conversão [1] binário, [2] octal, [3] hexadecimal: "))
if conversao == 1:
    print(f"o número convertido será {bin(número)}")
elif conversao == 2:
    print(f"o número convertido será {oct(número)}")
elif conversao == 3:
    print(f"o número convertido será {hex(número)}")
numero1 = int(input("Digite um valor:"))
numero2 = int(input("Digite um valor:"))
if numero1 > numero2:
    print(f"O valor {numero1} é maior do que o valor {numero2}")
elif numero1 < numero2:
    print(f"O valor {numero2} é maior do que o valor {numero1}")
elif numero1 == numero2:
    print(f"O valor {numero1} e {numero2} são iguais")
idade = int(input("Qual a sua idade?"))
if idade < 18:
    print(f"falta {18-idade} anos para se alistar")
elif idade == 18:
    print(f"é hora de alistar")
elif idade > 18:
    print(f"Ja possou {idade-18} anos do prazo")
media1 = int(input("Digite sua primeira nota:"))
media2 = int(input("Digite sua segunda nota:"))
media = (media1+media2)/2
if media < 5:
    print("Reprovado")
elif 5 <= media <= 6.9:
    print("Recuperação")
elif media >= 7:
    print("Aprovado")
idade = int(input("Digite sua idade:"))
if idade < 9:
    print("Mirim")
elif idade < 14:
     print("Infantil")
elif media < 19:
    print("Junior")
elif media < 20:
    print("Sênior")
elif idade >= 20:
    print("Master")
tri1 = int(input("O primeiro lado:"))
tri2 = int(input("O segundo lado:"))
tri3 = int(input("O terceiro lado:"))
if (tri1+tri2) < tri3:
    print("Não pode formar um triângulo")
elif (tri1+tri3) < tri2:
    print("Não pode formar um triângulo")
elif (tri2+tri3) < tri1:
    print("Não pode formar um triângulo")
else:
    if (tri2 == tri1 and tri1 == tri3) and tri2 == tri3:
        print("Este é um triângulo equilátero")
    elif (tri2 != tri1 and tri1 != tri3) and tri2 != tri3:
        print("Este é um triângulo escaleno")
    else:
        print("Este é um triângulo isósceles")
Peso = int(input("Qual o seu peso:"))
Altura = int(input("Qual a sua altura:"))
IMC = Peso/(Altura**2)
if IMC < 18.5:
    print("Abaixo do Peso")
elif 18.5 <= IMC < 25:
    print("Peso ideial")
elif 25 <= IMC < 30:
    print("Sobrepeso")
elif 30 <= IMC < 40:
    print("Obesidade ")
elif IMC > 40:
    print("Obesidade mórbida")
ProNor = int(input("Qual o seu preço normal?"))
Cond = str(input("Qual a sua condição de pagamento?"))
if Cond == 'Dinheiro' or Cond == 'Cheque':
    print(f"A conta fica {ProNor - (ProNor*0.10)}")
elif Cond == 'Cartão':
    print(f"A conta fica {ProNor - (ProNor*0.05)}")
elif Cond == '2x no Cartão':
    print(f"A conta fica {ProNor}")
else:
    print(f"A conta fica {ProNor + (ProNor*0.20)}")