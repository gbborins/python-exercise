word = str(input("Digite a expressão:"))
pare = []
for i in word:
    if i == '(' or i== ')':
        pare.append(i)
while '(' in pare and ')' in pare:
    for t, i in enumerate(pare):
        if (pare[t] == '(' and pare[t+1] == ')'):
            pare.pop(t)
            pare.pop(t)
if pare != []:
    print("Sua expressão está incorreta")
else:
    print("Sua expressão está correta")