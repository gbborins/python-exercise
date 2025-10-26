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