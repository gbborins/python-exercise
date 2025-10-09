#Exer 95
list = []
res = ''
while True:
    if res.lower() == 'n':
        break
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
    for j,k in enumerate(jogo['partida']):
        total += k
    jogo['total'] = total
    list.append(jogo)
    res = str(input("Quer continuar S/N?"))
print("Cod. Nome. Gols. Total.")
for j,i in enumerate(list):
    print(f"{j} {i['nome']} {i['partida']} {i['total']}")
while True:
    dados = int(input("Dados de qual jogador? (999 para)"))
    if dados == 999:
        break
    try:
        if list[dados]:
            print(f"Levantamento do jogador {list[dados]['nome']}")
            for k,l in enumerate(list[dados]['partida']):
                print(f"No jogo {k} fez {l}")
    except IndexError:
        print("ERRO! Não existe o jogador")