# receber uma String e número inteiro como entrada do usuário, depois realizar um loop dessa String de acordo com o número digitado 

# Recebe uma string do usuário
texto = input("Digite um texto: ")

# Recebe um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Repete a string o número de vezes informado
resultado = (texto + " ") * numero

# Exibe o resultado
print("Resultado:", resultado)
