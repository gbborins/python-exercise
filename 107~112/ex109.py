from ex109s import moeda
pre = float(input("Digite um preço: R$"))
por = int(input("Digite a porcentagem de aumento/diminuição: "))
show = str(input("Mostrar a formatação True/False: "))
while True:
    if show == 'True' or show == '':
        show = True
        break
    elif show == 'False':
        show = False
        break
    else:
        show = str(input("Mostrar a formatação True/False: "))
print(f'A medade de {moeda.moeda(pre)} é {moeda.metade(pre, mos = show)}')
print(f'O dobro de {moeda.moeda(pre)} é {moeda.dobro(pre, mos = show)}')
print(f'Aumentando {por}% é {moeda.aumentar(pre,por, mos = show)}')
print(f'Diminuindo {por}% é {moeda.diminuir(pre,por, mos = show)}')