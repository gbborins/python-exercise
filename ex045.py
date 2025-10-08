import random
jogada = int(input("Qual a sua jogada?\n 1. - Pedra\n 2. - Papel\n 3. - Tesoura\n "))
comp = random.randint(1,3)
# 1 = pedra, 2 = papel, 3 = tesoura
if jogada == 1:
    if comp == 2:
        print(f'o computador jogou {comp}')
        print("Você perdeu")
    if comp == 3:
        print(f'o computador jogou {comp}')
        print("Você ganhou")
elif jogada == 2:
    if comp == 1:
        print(f'o computador jogou {comp}')
        print("Você ganhou")
    if comp == 3:
        print(f'o computador jogou {comp}')
        print("Você perdeu")
elif jogada == 3:
    if comp == 1:
        print(f'o computador jogou {comp}')
        print("Você perdeu")
    if comp == 2:
        print(f'o computador jogou {comp}')
        print("Você ganhou")
else:
    print(f'o computador jogou {comp}')
    print("Empate")