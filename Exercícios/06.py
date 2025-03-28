turno = str(input("Digite o seu turno, Matutino = M, Vespertino = V ou Noturno = N: ")).upper()
if turno == 'M':
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido")