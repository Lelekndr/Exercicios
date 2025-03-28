
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2


print("Números em ordem crescente:", num1, num2, num3)
