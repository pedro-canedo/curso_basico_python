#calculo de imc e igual a peso dividido por altura ao quadrado

peso = float(input("Digite seu peso: ")) 
altura = float(input("Digite sua altura: "))

calcula_imc = peso / (altura * altura)

print(f"Seu imc é {calcula_imc:.2f}")


#se eu estou ou nao acima do peso e qual e o meu peso ideal
