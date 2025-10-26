def aumentar(n, dis):
    return n + n * dis / 100
def diminuir(n, dis):
    return n - n * dis / 100
def dobro(n):
    return n * 2
def metade(n):
    return n / 2
def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')