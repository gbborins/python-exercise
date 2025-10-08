tre = ('aprender','programar','linguagem','python','curso',
       'gratis','estudar','praticar','trabalhar',
       'mercado','programador','futuro')
for tur in tre:
    print(f"\nO {tur} tem as seguintes vogais:", end='')
    for letra in tur:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')