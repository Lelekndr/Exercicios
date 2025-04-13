total_pessoas = 25

idade_mais_velha = 0
altura_mais_alta = 0
maior_peso = 0

soma_alturas = 0
soma_imc = 0

masculinos = 0
femininos = 0

print("== Coleta de dados da Academia BemMaisFort ==")

for i in range(1, total_pessoas + 1):
    print(f"\nPessoa {i}:")

    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    altura = float(input("Altura (em metros): "))
    peso = float(input("Peso (em kg): "))

    # Atualiza dados extremos
    if idade > idade_mais_velha:
        idade_mais_velha = idade

    if altura > altura_mais_alta:
        altura_mais_alta = altura

    if peso > maior_peso:
        maior_peso = peso

    # Soma para médias
    soma_alturas += altura
    imc = peso / (altura ** 2)
    soma_imc += imc

    # Contagem de sexo
    if sexo == 'M':
        masculinos += 1
    elif sexo == 'F':
        femininos += 1

# Cálculo de médias e porcentagens
media_altura = soma_alturas / total_pessoas
media_imc = soma_imc / total_pessoas

porcent_masculino = (masculinos / total_pessoas) * 100
porcent_feminino = (femininos / total_pessoas) * 100

# Resultados finais
print("\n== RESULTADOS FINAIS ==")
print(f"Idade da pessoa mais velha: {idade_mais_velha} anos")
print(f"Altura da pessoa mais alta: {altura_mais_alta:.2f} m")
print(f"Maior peso: {maior_peso:.1f} kg")
print(f"Média de altura: {media_altura:.2f} m")
print(f"Média de IMC: {media_imc:.2f}")
print(f"Porcentagem de sexo masculino: {porcent_masculino:.1f}%")
print(f"Porcentagem de sexo feminino: {porcent_feminino:.1f}%")
