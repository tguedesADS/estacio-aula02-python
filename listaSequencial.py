# 1) Faça um Programa que mostre a mensagem "Alo mundo" na tela.
x = "Alo mundo"
print(x)

# 2)Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = int(input("Digite um número: "))
print(f"O número informado foi {numero}")

# 3) Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média do bimestre é {media}")

# 4) Faça um Programa que converta metros para centímetros.
metros = int(input("Digite a quantidade em metros: "))
conversor = metros * 100
print(f"{metros}m é igual a {conversor}cm")

# 5) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = int(input("Digite o raio de um círuculo: "))
area = 3.14 * (raio ** 2)
print(f"A área do círculo é {area}")

# 6) Faça um Programa que calcule a área de um quadrado
base = int(input("Digite a base do quadrado: "))
altura = int(input("Digite a altura do quadrado: "))
areaQuadrado = base * altura
print(f"A área do quadrado é {areaQuadrado}")

# 7) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_total = valor_por_hora * horas_trabalhadas
print(f"Seu salário total no mês é: R${salario_total:.2f}")

# 8) Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
Fahrenheit = float(input("Entre com a temperatura em graus Fahrenheit: "))
Celsius = (Fahrenheit - 32) * 5/9
print(f"Valor em Celsius: {Celsius:.2f}°C")

# 9) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a)o produto do dobro do primeiro com metade do segundo .
# b)a soma do triplo do primeiro com o terceiro.
# c)o terceiro elevado ao cubo.
numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))
resultado_a = (2 * numero_inteiro1) * (numero_inteiro2 / 2)
resultado_b = (3 * numero_inteiro1) + numero_real
resultado_c = numero_real ** 3
print(f"a) O produto do dobro do primeiro com metade do segundo é: {resultado_a}")
print(f"b) A soma do triplo do primeiro com o terceiro é: {resultado_b}")
print(f"c) O terceiro elevado ao cubo é: {resultado_c}")

# 10) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58
altura_pessoa = float(input("Digite a altura da pessoa em metros: "))
peso_ideal = (72.7 * altura) - 58
print(f"O peso ideal para a altura {altura}m é: {peso_ideal:.2f}kg")


