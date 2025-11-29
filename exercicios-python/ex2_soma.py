def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a // b

def exibir_menu():
    print("\n=== Calculadora Básica ===")
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[0] Sair")

while True:
    exibir_menu()
    opcao = input("Escolha: ").strip()

    if opcao == "0":
        print("Encerrando...")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida!")
        continue

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", somar(num1, num2))
    elif opcao == "2":
        print("Resultado:", subtrair(num1, num2))
    elif opcao == "3":
        print("Resultado:", multiplicar(num1, num2))
    elif opcao == "4":
        print("Resultado:", dividir(num1, num2))