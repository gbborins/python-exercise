def aumentar(n, dis, mos = True):
    n += n*dis/100
    if mos == True:
        n = moeda(n)
    return n
def diminuir(n, dis, mos = True):
    n -= n*dis/100
    if mos == True:
        n = moeda(n)
    return n
def dobro(n, mos = True):
    n *= 2
    if mos == True:
        n = moeda(n)
    return n
def metade(n, mos = True):
    n /= 2
    if mos == True:
        n = moeda(n)
    return n
def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')
def resumo(n, dis, most = True):
    print('-'*40)
    print(' '*10, end='')
    print('RESUMO DO VALOR', end='')
    print(' '*10)
    print('-'*40)
    print(f'A medade de {moeda(n)} é {metade(n, mos = most)}')
    print(f'O dobro de {moeda(n)} é {dobro(n, mos = most)}')
    print(f'Aumentando {dis}% é {aumentar(n,dis, mos = most)}')
    print(f'Diminuindo {dis}% é {diminuir(n,dis, mos = most)}')
    print('-'*40)