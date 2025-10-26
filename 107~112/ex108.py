from ex108s import moeda
pre = float(input("Digite um preço: R$"))
por = float(input("Digite a porcentagem de aumento/diminuição: "))
print(f'A medade de {moeda.moeda(pre)} é {moeda.moeda(moeda.metade(pre))}')
print(f'O dobro de {moeda.moeda(pre)} é {moeda.moeda(moeda.dobro(pre))}')
print(f'Aumentando {por}% é {moeda.moeda(moeda.aumentar(pre,por))}')
print(f'Diminuindo {por}% é {moeda.moeda(moeda.diminuir(pre,por))}')