# receber dois números como entrada do usuário e realizar uma operação matemática simples (valores absolutos)

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

operação = input("Digite a operação que deseja realizar (+, -, / ou *): ")

if operação == '+':
    print(numero1 + numero2)
elif operação == '-':
    print(abs(numero1 - numero2))
elif operação == '/':
    if numero2 != 0:
        print(numero1 / numero2)
    else:
        print("Não há divisão por 0!")
elif operação == '*':
    print(numero1 * numero2)
else:
    print("Operação inválida!")