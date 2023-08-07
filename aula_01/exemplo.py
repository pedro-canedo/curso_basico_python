#  Exemplos práticos de código
# Exemplo 1: Calculadora de IMC



peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# imc e igual a peso dividido por altura ao quadrado
imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.2f}")
#o :.2f é para formatar o número com duas casas decimais
#sobre peso
#dentro peso
#abaixo do peso