
votos = {
    "José": 0,
    "João": 0,
    "Maria": 0,
    "Ana": 0,
    "Nulo": 0,
    "Branco": 0
}

print("Digite os votos (0 para encerrar):")
print("1 - José | 2 - João | 3 - Maria | 4 - Ana | 5 - Nulo | 6 - Branco")

while True:
    codigo = int(input("Código do voto: "))

    if codigo == 0:
        break
    elif codigo == 1:
        votos["José"] += 1
    elif codigo == 2:
        votos["João"] += 1
    elif codigo == 3:
        votos["Maria"] += 1
    elif codigo == 4:
        votos["Ana"] += 1
    elif codigo == 5:
        votos["Nulo"] += 1
    elif codigo == 6:
        votos["Branco"] += 1
    else:
        print("Código inválido! Tente novamente.")


total_votos = sum(votos.values())


porcent_nulo = (votos["Nulo"] / total_votos) * 100 if total_votos > 0 else 0
porcent_branco = (votos["Branco"] / total_votos) * 100 if total_votos > 0 else 0


print("\nRESULTADO DA VOTAÇÃO:")
print(f"José: {votos['José']} votos")
print(f"João: {votos['João']} votos")
print(f"Maria: {votos['Maria']} votos")
print(f"Ana: {votos['Ana']} votos")
print(f"Nulos: {votos['Nulo']} votos")
print(f"Brancos: {votos['Branco']} votos")
print(f"\nPercentual de votos nulos: {porcent_nulo:.2f}%")
print(f"Percentual de votos em branco: {porcent_branco:.2f}%")
