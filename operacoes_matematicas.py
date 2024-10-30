# Vamos solicitar como entrada dois números e depois vamos realizar uma opração simples entre eles.

# Solicita o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número
numero2 = float(input("Digite o segundo número: "))

# Solicita a operação
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação com base na escolha do usuário
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = abs(numero1 - numero2)  # Usa valor absoluto para subtração
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

# Exibe o resultado
print("O resultado é:", resultado)
