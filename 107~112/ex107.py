from ex107s import moeda
pre = float(input("Digite um preço: R$"))
por = float(input("Digite a porcentagem de aumento/diminuição: "))
print(f'A medade de R${pre} é {moeda.metade(pre)}')
print(f'O dobro de R${pre} é {moeda.metade(pre)}')
print(f'Aumentando {por}% é {moeda.aumentar(pre, por)}')
print(f'Diminuindo {por}% é {moeda.diminuir(pre, por)}')