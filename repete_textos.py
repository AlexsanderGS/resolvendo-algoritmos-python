# Solicite uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Solicita a string do usuário
texto = input("Digite uma string: ")

# Solicita o número de repetições e converte para inteiro
n = int(input("Digite um número inteiro: "))

# Repete a string n vezes
resultado = " ".join([texto] * n)

# Exibe o resultado
print("A string repetida é:", resultado)
