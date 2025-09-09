def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multi(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Impossível dividir por 0"
    return a / b

def main():
    print("Calculadora inicial")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    choice = input("Escolha (1/2/3/4): ")
    num1 = float(input("Digite o priemiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if choice == '1':
        print(f"{num1} + {num2} = {soma(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtracao(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multi(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divisao(num1, num2)}")
    else:
        print("Erro")