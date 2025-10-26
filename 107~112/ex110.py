from ex110s import moeda
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
moeda.resumo(pre,por,most = show)