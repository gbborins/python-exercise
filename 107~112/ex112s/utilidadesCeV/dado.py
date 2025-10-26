def leiaDinheiro(pre):
    while True:
        if pre.isnumeric():
            pre = float(pre)
            return pre
        else:
            print('Erro monetário')
            pre = input("Digite um preço: R$")
def leiaPorcentagem(por):
    while True:
        if por.isnumeric():
            por = float(por)
            return por
        else:
            print('Erro monetário')
            por = input("Digite a porcentagem de aumento/diminuição: ")
        