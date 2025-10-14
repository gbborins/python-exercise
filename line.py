last = int(input(f"quantidade inicial"))
line = list(range(1,last+1))
while True:
    print(f"{len(line)} clientes restantes")
    print(f"fila atual: {line}")
    choice = str(input("Digite C(adicionar cliente), A(atendimento), F(fechar)))

