#Exer106
import pydoc
cores = {
    'padrao': '\033[m',
    'vermelho': '\033[0;30;41m',
    'verde': '\033[0;30;42m',
    'amarelo': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'roxo': '\033[0;30;45m',
    'branco': '\033[7;30m'
}
def he(ent):
    model(f"Acessando o manual do comando {ent}", 'azul')
    obj = eval(ent)
    texto = pydoc.render_doc(obj)
    print(cores['branco'] + texto + cores['padrao'])
def model(tex, cor='padrao'):
    lem = len(tex) + 4
    print(cores[cor], end='')
    print('~'*lem)
    print(f"  {tex}")
    print('~' * lem)
    print(cores['padrao'], end='')
model('SISTEMA DE AJUDA PyHELP', 'verde')
entrada = str(input("Funcao ou Biblioteca > "))
while True:
    if entrada.lower() == 'fim':
        model('ATÉ LOGO!', 'vermelho')
        break
    he(entrada)
    entrada = input("Funcao ou Biblioteca > ")